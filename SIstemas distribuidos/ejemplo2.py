from mpi4py import MPI  
import numpy as np  

comm = MPI.COMM_WORLD  
size = comm.Get_size()  
rank = comm.Get_rank() 

# Datos iniciales en el proceso raíz
if rank == 0:
    data = np.arange(size * 10, dtype='d')  # Crear array con valores numéricos consecutivos
else:
    data = None  # Los demás procesos inicializan data como None

# Crear un array para recibir datos en cada proceso
recvbuf = np.empty(10, dtype='d')  # Array vacío para almacenar los datos recibidos

# Operaciones no bloqueantes de scatter y gather
req = comm.Iscatter(data, recvbuf, root=0)  # Scatter no bloqueante desde el proceso raíz
req.Wait()  # Esperar a que la operación de scatter se complete

# Cada proceso realiza alguna operación sobre sus datos
recvbuf = recvbuf**2  # Elevar al cuadrado los elementos en recvbuf

# Buffer para recopilar resultados
if rank == 0:
    gathered_data = np.empty(size * 10, dtype='d')  # Array vacío para almacenar datos recopilados
else:
    gathered_data = None  # Los demás procesos inicializan gathered_data como None

req = comm.Igather(recvbuf, gathered_data, root=0)  # Gather no bloqueante hacia el proceso raíz
req.Wait()  # Esperar a que la operación de gather se complete

# Proceso raíz realiza reducción colectiva para calcular la media
if rank == 0:
    mean_value = np.mean(gathered_data)  # Calcular la media de los datos recopilados
    print(f"Media de los cuadrados: {mean_value}")  # Imprimir el resultado
