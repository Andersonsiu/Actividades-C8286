from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor as Executor
from time import sleep
# Codigo de Tiago Rodriguez

def report_progress(futures, tag, callback):
    # Inicializa los contadores de tareas completadas y no completadas.
    not_done = 1
    done = 0
    # Bucle mientras haya tareas no completadas.
    while not_done > 0:
        not_done = 0
        done = 0
        # Itera sobre cada futuro para verificar si está completado.
        for fut in futures:
            if fut.done():
                done += 1  # Incrementa el contador de completadas.
            else:
                not_done += 1  # Incrementa el contador de no completadas.
        # Pausa el bucle por medio segundo para reducir la carga de comprobación.
        sleep(0.5)
        # Si hay una función de callback, informa el progreso actual.
        if callback:
            callback(tag, done, not_done)
    

def async_map(executor, mapper, data):
    # Lista para almacenar los futuros.
    futures = []
    # Envía cada elemento de los datos a la función mapper usando el executor.
    for datum in data:
        futures.append(executor.submit(mapper, datum))
    # Devuelve la lista de futuros.
    return futures


def map_less_naive(executor, my_input, mapper):
    # Aplica la función de mapeo a cada entrada y devuelve los resultados.
    map_results = async_map(executor, mapper, my_input)
    return map_results


def map_reduce_less_naive(my_input, mapper, reducer, callback=None):
    # Crea un ejecutor con un máximo de dos trabajadores.
    with Executor(max_workers=2) as executor:
        # Mapea las entradas y monitorea el progreso.
        futures = async_map(executor, mapper, my_input)
        report_progress(futures, 'map', callback)
        # Obtiene los resultados del mapeo.
        map_results = map(lambda f: f.result(), futures)
        # Agrupa los resultados por clave.
        distributor = defaultdict(list)
        for key, value in map_results:
            distributor[key].append(value)

        # Realiza el proceso de reducción y monitorea el progreso.
        futures = async_map(executor, reducer, distributor.items())
        report_progress(futures, 'reduce', callback)
        # Obtiene los resultados de la reducción.
        results = map(lambda f: f.result(), futures)
    # Devuelve los resultados finales.
    return results


def emitter(word):
    # Función de mapeo que emite cada palabra con un conteo inicial de 1.
    return word, 1


def counter(emitted):
    # Función de reducción que suma los conteos de cada palabra.
    return emitted[0], sum(emitted[1])


def reporter(tag, done, not_done):
    # Imprime el estado del progreso para la operación actual.
    print(f'Operacion {tag}: {done}/{done+not_done}')

# Prepara los datos y ejecuta el proceso MapReduce.
words = 'Python es super Python rocks'.split(' ')
a = map_reduce_less_naive(words, emitter, counter, reporter)

# Imprime los resultados ordenados por frecuencia.
for i in sorted(a, key=lambda x: x[1]):
    print(i)
