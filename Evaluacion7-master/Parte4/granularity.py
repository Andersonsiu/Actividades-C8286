from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor as Executor
from time import time, sleep

def report_progress(futures, tag, callback):
    not_done = 1
    done = 0
    while not_done > 0:
        not_done = 0
        done = 0
        for fut in futures:
            if fut.done():
                done += 1
            else:
                not_done += 1
        sleep(0.5)
        if callback:
            callback(tag, done, not_done)

def async_map(executor, mapper, data):
    futures = []
    for datum in data:
        futures.append(executor.submit(mapper, datum))
    return futures

def map_reduce_granularity(my_input, mapper, reducer, chunk_size, callback=None):
    with Executor(max_workers=4) as executor:
        chunks = [my_input[i:i + chunk_size] for i in range(0, len(my_input), chunk_size)]
        futures = []
        for chunk in chunks:
            futures.extend(async_map(executor, mapper, chunk))
        report_progress(futures, 'map', callback)
        map_results = [f.result() for f in futures]
        distributor = defaultdict(list)
        for key, value in map_results:
            distributor[key].append(value)
        futures = async_map(executor, reducer, distributor.items())
        report_progress(futures, 'reduce', callback)
        results = [f.result() for f in futures]
    return results

def emitter(word):
    return word, 1

def counter(emitted):
    return emitted[0], sum(emitted[1])

def reporter(tag, done, not_done):
    print(f'Operacion {tag}: {done}/{done+not_done}')

def test_granularity(words):
    for chunk_size in [1, 2, 4, 8, 16]:
        start_time = time()
        results = map_reduce_granularity(words, emitter, counter, chunk_size, reporter)
        end_time = time()
        print(f'Chunk Size: {chunk_size}, Time: {end_time - start_time}')
        for i in sorted(results, key=lambda x: x[1]):
            print(i)

if __name__ == '__main__':
    words = 'Python es super Python rocks'.split(' ')
    test_granularity(words)
