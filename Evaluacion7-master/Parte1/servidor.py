import asyncio
import pickle
from random import randint

results = {}

async def submit_job(reader, writer):
    job_id = max(list(results.keys()) + [0]) + 1
    writer.write(job_id.to_bytes(4, 'little'))
    await writer.drain()
    sleep_time = randint(1, 4)
    await asyncio.sleep(sleep_time)
    results[job_id] = sleep_time

async def get_results(reader, writer):
    job_id = int.from_bytes(await reader.read(4), 'little')
    data = pickle.dumps(results.get(job_id, None))
    writer.write(len(data).to_bytes(4, 'little'))
    writer.write(data)
    await writer.drain()

async def sum_numbers(reader, writer):
    job_id = max(list(results.keys()) + [0]) + 1
    writer.write(job_id.to_bytes(4, 'little'))
    await writer.drain()
    data_size = int.from_bytes(await reader.read(4), 'little')
    data = await reader.read(data_size)
    numbers = pickle.loads(data)
    result = sum(numbers)
    results[job_id] = result

import concurrent.futures

executor = concurrent.futures.ProcessPoolExecutor()

async def cpu_intensive_task(reader, writer):
    job_id = max(list(results.keys()) + [0]) + 1
    writer.write(job_id.to_bytes(4, 'little'))
    await writer.drain()
    data_size = int.from_bytes(await reader.read(4), 'little')
    data = await reader.read(data_size)
    numbers = pickle.loads(data)
    
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(executor, sum, numbers)
    
    results[job_id] = result

async def accept_requests(reader, writer):
    op = await reader.read(1)
    if op[0] == 0:
        await submit_job(reader, writer)
    elif op[0] == 1:
        await get_results(reader, writer)
    elif op[0] == 2:
        await sum_numbers(reader, writer)
    elif op[0] == 3:
        await long_running_task(reader, writer)
    elif op[0] == 4:
        await cpu_intensive_task(reader, writer)
    writer.close()
    await writer.wait_closed()


async def long_running_task(reader, writer):
    job_id = max(list(results.keys()) + [0]) + 1
    writer.write(job_id.to_bytes(4, 'little'))
    await writer.drain()
    task_complexity = int.from_bytes(await reader.read(4), 'little')
    await asyncio.sleep(task_complexity)
    results[job_id] = f"Completed task with complexity {task_complexity}"


async def main():
    server = await asyncio.start_server(accept_requests, '127.0.0.1', 1936)
    async with server:
        await server.serve_forever()

asyncio.run(main())
