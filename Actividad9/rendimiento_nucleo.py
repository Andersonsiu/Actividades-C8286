import multiprocessing

def core_affinity_worker(core_id, shared_data, start, end):
    p = multiprocessing.current_process()
    p.cpu_affinity([core_id])  # Asigna el núcleo específico
    for i in range(start, end):
        shared_data[i] += 1

size = 10**6
shared_data = np.zeros(size)
num_processes = 4
processes = []

chunk_size = size // num_processes
for i in range(num_processes):
    start = i * chunk_size
    end = (i + 1) * chunk_size
    process = multiprocessing.Process(target=core_affinity_worker, args=(i, shared_data, start, end))
    processes.append(process)

start_time = time.perf_counter()

for process in processes:
    process.start()

for process in processes:
    process.join()

end_time = time.perf_counter()
total_time = end_time - start_time

print(f"Tiempo total con afinidad de núcleo y {num_processes} procesos: {total_time:.6f} segundos")
