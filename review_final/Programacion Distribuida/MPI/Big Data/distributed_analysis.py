# distributed_analysis.py
from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Tamaño total del conjunto de datos
data_size = 1000000
chunk_size = data_size // size

# Crear un conjunto de datos masivo solo en el proceso raíz
if rank == 0:
    data = np.random.random(data_size)
else:
    data = None

# Cada nodo recibe un fragmento del conjunto de datos
chunk = np.empty(chunk_size, dtype='d')
reqs = []

# Enviar y recibir datos de manera no bloqueante
if rank == 0:
    for i in range(1, size):
        reqs.append(comm.Isend([data[i * chunk_size:(i + 1) * chunk_size], MPI.DOUBLE], dest=i))
    chunk = data[0:chunk_size]
else:
    reqs.append(comm.Irecv(chunk, source=0))

MPI.Request.Waitall(reqs)
print(f"Proceso {rank} completó la comunicación no bloqueante.")

# Filtrar datos (ejemplo: mantener solo valores mayores a 0.5)
filtered_chunk = chunk[chunk > 0.5]

# Transformar datos (ejemplo: elevar al cuadrado)
transformed_chunk = filtered_chunk ** 2

# Calcular la suma local
local_sum = np.sum(transformed_chunk)
local_count = len(transformed_chunk)

# Reducir para obtener la suma global y el recuento global
global_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)
global_count = comm.reduce(local_count, op=MPI.SUM, root=0)

if rank == 0:
    global_mean = global_sum / global_count
    print(f"Media global: {global_mean}")

# Difundir la media global a todos los nodos
global_mean = comm.bcast(global_mean if rank == 0 else None, root=0)

print(f"Proceso {rank} conoce la media global: {global_mean}")


#mpirun -np 4 python distributed_analysis.py

