from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor as Executor, as_completed
import os

# Definimos las funciones de mapeo y reducción
def map_function(word):
    return (word, 1)

def reduce_function(item):
    word, counts = item
    return (word, sum(counts))

# Función para realizar MapReduce con seguimiento del progreso
def map_reduce_with_progress(my_input, mapper, reducer):
    # Distribuye los resultados del mapeo
    distributor = defaultdict(list)

    # Inicia un ejecutor de hilos
    with Executor() as executor:
        # Primero, ejecutamos el mapeo
        future_to_word = {executor.submit(mapper, word): word for word in my_input}
        for future in as_completed(future_to_word):
            word, count = future.result()
            distributor[word].append(count)

        # Después, ejecutamos la reducción
        results = executor.map(reducer, distributor.items())
    
    # Convertimos los resultados a una lista y retornamos
    return list(results)

# Preparamos los datos de entrada leyendo desde un archivo
def prepare_data(file_path):
    with open(file_path, 'rt', encoding='utf-8') as file:
        # Limpiamos y dividimos las palabras, filtramos las cadenas vacías
        words = filter(None, [word.strip().rstrip() for line in file for word in line.split()])
    return words

# Ejecutamos el proceso de MapReduce
if __name__ == "__main__":
    words = prepare_data('texto.txt')
    results = map_reduce_with_progress(words, map_function, reduce_function)

    # Ordenamos los resultados y los imprimimos
    for word, count in sorted(results, key=lambda x: x[1], reverse=True):
        print(f"Palabra: '{word}', Frecuencia: {count}")
