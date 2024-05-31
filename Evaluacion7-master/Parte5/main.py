import asyncio
import marshal
import multiprocessing as mp
import pickle
from queue import Empty, Queue
import threading
import types

import chunk_mp_mapreduce as mr

work_queue = Queue()
results_queue = Queue()
results = {}

async def submit_job(job_id, reader, writer):
    writer.write(job_id.to_bytes(4, 'little'))
    await writer.drain()
    code_size = int.from_bytes(await reader.read(4), 'little')
    my_code = marshal.loads(await reader.read(code_size))
    data_size = int.from_bytes(await reader.read(4), 'little')
    data = pickle.loads(await reader.read(data_size))
    work_queue.put_nowait((job_id, my_code, data))

def get_results_queue():
    while results_queue.qsize() > 0:
        try:
            job_id, data = results_queue.get_nowait()
            results[job_id] = data
        except Empty:
            return

async def get_results(reader, writer):
    get_results_queue()
    job_id = int.from_bytes(await reader.read(4), 'little')
    data = pickle.dumps(None)
    if job_id in results:
        data = pickle.dumps(results[job_id])
        del results[job_id]
    writer.write(len(data).to_bytes(4, 'little'))
    writer.write(data)
    await writer.drain()

async def accept_requests(reader, writer, job_id=[0]):
    op = await reader.read(1)
    if op[0] == 0:
        await submit_job(job_id[0], reader, writer)
        job_id[0] += 1
    elif op[0] == 1:
        await get_results(reader, writer)

def worker():
    pool = mp.Pool()
    while True:
        job_id, code, data = work_queue.get()
        func = types.FunctionType(code, globals(), 'mapper_and_reducer')
        mapper, reducer = func()
        counts = mr.mapreduce.map_reduce(pool, data, mapper, reducer, 100, mr.reporting.report_progress)
        results_queue.put((job_id, counts))
    pool.close()
    pool.join()

async def main():
    server = await asyncio.start_server(accept_requests, '127.0.0.1', 1936)
    worker_thread = threading.Thread(target=worker)
    worker_thread.start()
    async with server:
        await server.serve_forever()

asyncio.run(main())
