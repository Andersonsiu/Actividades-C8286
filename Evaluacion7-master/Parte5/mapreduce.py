from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor as Executor
from .reporting import report_progress

def async_map(executor, mapper, data):
    futures = []
    for datum in data:
        futures.append(executor.submit(mapper, datum))
    return futures

def map_reduce_less_naive(my_input, mapper, reducer, callback=None, num_processes=2):
    with Executor(max_workers=num_processes) as executor:
        futures = async_map(executor, mapper, my_input)
        report_progress(futures, 'map', callback)
        map_results = [f.result() for f in futures]
        distributor = defaultdict(list)
        for key, value in map_results:
            distributor[key].append(value)
        futures = async_map(executor, reducer, distributor.items())
        report_progress(futures, 'reduce', callback)
        results = [f.result() for f in futures]
    return results

def map_reduce(pool, data, mapper, reducer, chunk_size, callback):
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    futures = []
    for chunk in chunks:
        futures.append(pool.apply_async(mapper, (chunk,)))
    report_progress(futures, 'map', callback)
    map_results = [f.get() for f in futures]
    distributor = defaultdict(list)
    for key, value in map_results:
        distributor[key].append(value)
    futures = []
    for key, value in distributor.items():
        futures.append(pool.apply_async(reducer, ((key, value),)))
    report_progress(futures, 'reduce', callback)
    results = [f.get() for f in futures]
    return results
