import multiprocessing
from functools import reduce

def square(n):
    """Devuelve el cuadrado de un número."""
    return n * n

def add(x, y):
    """Suma dos números."""
    return x + y

def parallel_sum_of_squares(numbers):
    """Calcula la suma de los cuadrados de una lista de números distribuidos entre varios procesos."""
    # Obtener el número de núcleos de CPU disponibles
    pool_size = multiprocessing.cpu_count()
    
    # Crear un pool de procesos con el número de núcleos disponibles
    with multiprocessing.Pool(processes=pool_size) as pool:
        # Distribuir el cálculo del cuadrado de cada número a través del pool
        squares = pool.map(square, numbers)
        # Reducir la lista de cuadrados sumándolos
        result = reduce(add, squares)
    
    return result

# Lista de números
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ejecutar la función y mostrar el resultado
result = parallel_sum_of_squares(numbers)
print("La suma de los cuadrados es:", result)
