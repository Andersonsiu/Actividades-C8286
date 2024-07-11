# distribute_data.py
from mpi4py import MPI
import numpy as np

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
comm.Scatter(data, chunk, root=0)

print(f"Proceso {rank} recibió {chunk_size} elementos.")
