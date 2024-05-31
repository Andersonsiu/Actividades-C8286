import asyncio
import pickle
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import logging

logging.basicConfig(level=logging.INFO)

results = {}
executor = ThreadPoolExecutor(max_workers=4)

def safe_execute(func, *args):
    try:
        return func(*args)
    except Exception as e:
        logging.error(f"Error ejecutando {func.__name__}: {e}")
        return None

def map_reduce_ultra_naive_parallel(my_input, mapper, reducer):
    logging.info("Inicio de MapReduce")

    try:
        with ThreadPoolExecutor() as executor:
            map_results = list(executor.map(lambda word: safe_execute(mapper, word), my_input))

        distributor = defaultdict(list)
        for key, value in map_results:
            if value is not None:
                distributor[key].append(value)

        with ThreadPoolExecutor() as executor:
            reduced_results = list(executor.map(lambda item: safe_execute(reducer, item), distributor.items()))

        logging.info("Fin de MapReduce")
        return reduced_results
    except Exception as e:
        logging.error(f"Error durante MapReduce: {e}")
        raise

async def map_reduce(reader, writer):
    job_id = max(list(results.keys()) + [0]) + 1
    writer.write(job_id.to_bytes(4, 'little'))
    await writer.drain()
    data_size = int.from_bytes(await reader.read(4), 'little')
    data = await reader.read(data_size)
    words = pickle.loads(data)

    emiter = lambda word: (word, 1)
    counter = lambda emitted: (emitted[0], sum(emitted[1]))

    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(executor, map_reduce_ultra_naive_parallel, words, emiter, counter)
    results[job_id] = result

async def get_results(reader, writer):
    job_id = int.from_bytes(await reader.read(4), 'little')
    data = pickle.dumps(results.get(job_id, None))
    writer.write(len(data).to_bytes(4, 'little'))
    writer.write(data)
    await writer.drain()

async def accept_requests(reader, writer):
    op = await reader.read(1)
    if op[0] == 5:
        await map_reduce(reader, writer)
    elif op[0] == 1:
        await get_results(reader, writer)
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(accept_requests, '127.0.0.1', 1936)
    async with server:
        await server.serve_forever()

asyncio.run(main())
