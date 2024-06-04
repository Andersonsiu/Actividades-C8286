from mpi4py import MPI
from threading import Thread

def thread_task(rank):
    print(f"Thread in rank {rank} is running")

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

threads = []
for _ in range(4):
    t = Thread(target=thread_task, args=(rank,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

if rank == 0:
    print("All threads completed.")
