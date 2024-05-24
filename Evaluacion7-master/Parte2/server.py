import asyncio
import pickle
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import random

results = {}
executor = ThreadPoolExecutor(max_workers=4)  # Número de hilos para paralelizar

def map_reduce_ultra_naive_parallel(my_input, mapper, reducer):
    with ThreadPoolExecutor() as executor:
        map_results = list(executor.map(mapper, my_input))

    distributor = defaultdict(list)
    for key, value in map_results:
        distributor[key].append(value)

    with ThreadPoolExecutor() as executor:
        reduced_results = list(executor.map(reducer, distributor.items()))

    return reduced_results

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

async def distributed_map_reduce(reader, writer):
    job_id = max(list(results.keys()) + [0]) + 1
    writer.write(job_id.to_bytes(4, 'little'))
    await writer.drain()
    data_size = int.from_bytes(await reader.read(4), 'little')
    data = await reader.read(data_size)
    words = pickle.loads(data)

    emiter = lambda word: (word, 1)
    counter = lambda emitted: (emitted[0], sum(emitted[1]))

    def node_mapper(words_chunk):
        return list(map(emiter, words_chunk))

    chunk_size = len(words) // 4
    chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]

    loop = asyncio.get_running_loop()
    map_results = await asyncio.gather(*[loop.run_in_executor(executor, node_mapper, chunk) for chunk in chunks])

    distributor = defaultdict(list)
    for map_result in map_results:
        for key, value in map_result:
            distributor[key].append(value)

    result = list(map_reduce_ultra_naive_parallel(words, emiter, counter))
    results[job_id] = result

async def load_balanced_map_reduce(reader, writer):
    job_id = max(list(results.keys()) + [0]) + 1
    writer.write(job_id.to_bytes(4, 'little'))
    await writer.drain()
    data_size = int.from_bytes(await reader.read(4), 'little')
    data = await reader.read(data_size)
    words = pickle.loads(data)

    emiter = lambda word: (word, 1)
    counter = lambda emitted: (emitted[0], sum(emitted[1]))

    def node_mapper(words_chunk):
        return list(map(emiter, words_chunk))

    chunk_size = len(words) // 4
    chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]

    loop = asyncio.get_running_loop()
    map_results = await asyncio.gather(*[loop.run_in_executor(executor, node_mapper, chunk) for chunk in chunks])

    distributor = defaultdict(list)
    for map_result in map_results:
        for key, value in map_result:
            distributor[key].append(value)

    result = list(map_reduce_ultra_naive_parallel(words, emiter, counter))
    results[job_id] = result

async def fault_tolerant_map_reduce(reader, writer):
    job_id = max(list(results.keys()) + [0]) + 1
    writer.write(job_id.to_bytes(4, 'little'))
    await writer.drain()
    data_size = int.from_bytes(await reader.read(4), 'little')
    data = await reader.read(data_size)
    words = pickle.loads(data)

    emiter = lambda word: (word, 1)
    counter = lambda emitted: (emitted[0], sum(emitted[1]))

    def node_mapper(words_chunk):
        if random.random() < 0.2:  # Simula un fallo en el 20% de los casos
            raise Exception("Simulated node failure")
        return list(map(emiter, words_chunk))

    chunk_size = len(words) // 4
    chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]

    loop = asyncio.get_running_loop()
    futures = [loop.run_in_executor(executor, node_mapper, chunk) for chunk in chunks]

    map_results = []
    for future in futures:
        try:
            result = await future
            map_results.append(result)
        except Exception as e:
            print(f"Reassigning chunk due to failure: {e}")
            reassigned_future = loop.run_in_executor(executor, node_mapper, chunk)
            result = await reassigned_future
            map_results.append(result)

    distributor = defaultdict(list)
    for map_result in map_results:
        for key, value in map_result:
            distributor[key].append(value)

    result = list(map_reduce_ultra_naive_parallel(words, emiter, counter))
    results[job_id] = result

def map_reduce_with_combiner(my_input, mapper, reducer):
    try:
        with ThreadPoolExecutor() as executor:
            map_results = list(executor.map(mapper, my_input))

        combiner = defaultdict(list)
        for key, value in map_results:
            combiner[key].append(value)

        combined_results = {key: sum(values) for key, values in combiner.items()}

        distributor = defaultdict(list)
        for key, value in combined_results.items():
            distributor[key].append(value)

        with ThreadPoolExecutor() as executor:
            reduced_results = list(executor.map(reducer, distributor.items()))

        return reduced_results
    except Exception as e:
        print(f"Error during map-reduce: {e}")
        raise

async def optimized_map_reduce(reader, writer):
    job_id = max(list(results.keys()) + [0]) + 1
    writer.write(job_id.to_bytes(4, 'little'))
    await writer.drain()
    data_size = int.from_bytes(await reader.read(4), 'little')
    data = await reader.read(data_size)
    words = pickle.loads(data)

    emiter = lambda word: (word, 1)
    counter = lambda emitted: (emitted[0], sum(emitted[1]))

    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(executor, map_reduce_with_combiner, words, emiter, counter)
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
    elif op[0] == 6:
        await distributed_map_reduce(reader, writer)
    elif op[0] == 7:
        await load_balanced_map_reduce(reader, writer)
    elif op[0] == 8:
        await fault_tolerant_map_reduce(reader, writer)
    elif op[0] == 9:
        await optimized_map_reduce(reader, writer)
    elif op[0] == 1:
        await get_results(reader, writer)
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(accept_requests, '127.0.0.1', 1936)
    async with server:
        await server.serve_forever()

asyncio.run(main())


