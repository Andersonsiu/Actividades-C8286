from collections import defaultdict
from multiprocessing import Pool
from time import time
import logging

logging.basicConfig(level=logging.INFO)

def report_progress(futures, tag, callback):
    not_done = 1
    done = 0
    while not_done > 0:
        not_done = 0
        done = 0
        for fut in futures:
            if fut.ready():
                done += 1
            else:
                not_done += 1
        sleep(0.5)
        if callback:
            callback(tag, done, not_done)

def async_map(pool, mapper, data):
    futures = []
    for datum in data:
        futures.append(pool.apply_async(mapper, (datum,)))
    return futures

def map_reduce_pool(my_input, mapper, reducer, num_processes, callback=None):
    with Pool(processes=num_processes) as pool:
        futures = async_map(pool, mapper, my_input)
        report_progress(futures, 'map', callback)
        map_results = [f.result() for f in futures]
        distributor = defaultdict(list)
        for key, value in map_results:
            distributor[key].append(value)
        futures = async_map(pool, reducer, distributor.items())
        report_progress(futures, 'reduce', callback)
        results = [f.result() for f in futures]
    return results

def emitter(word):
    return word, 1

def counter(emitted):
    return emitted[0], sum(emitted[1])

def reporter(tag, done, not_done):
    print(f'Operacion {tag}: {done}/{done+not_done}')

def test_num_processes(words):
    for num_processes in [1, 2, 4, 8]:
        start_time = time()
        results = map_reduce_pool(words, emitter, counter, num_processes, reporter)
        end_time = time()
        print(f'Processes: {num_processes}, Time: {end_time - start_time}')
        for i in sorted(results, key=lambda x: x[1]):
            print(i)

if __name__ == '__main__':
    words = 'Python es super Python rocks'.split(' ')
    test_num_processes(words)
