from multiprocessing import Pool

# Definición de la función que suma los elementos de un segmento
def sum_segment(segment):
    return sum(segment)

if __name__ == "__main__":
    data = list(range(100))  # Crea una lista de mil elementos
    num_processes = 4  # Número de procesos a utilizar en el pool
    segment_size = len(data) // num_processes  # Calcula el tamaño de cada segmento

    # Divide la lista de datos en segmentos de tamaño igual
    #data[0 * 250 : (0 + 1) * 250]  # data[0 : 250]
    segments = [data[i * segment_size:(i + 1) * segment_size] for i in range(num_processes)]

    # Crea un pool de procesos y distribuye el trabajo entre ellos
    with Pool(num_processes) as pool:
        # Mapea la función sum_segment a cada uno de los segmentos en paralelo
        results = pool.map(sum_segment, segments)

    # Suma los resultados parciales para obtener la suma total
    total_sum = sum(results)
    # Imprime la suma total
    print(f"Total sum: {total_sum}")
    print(f"segmentos:{segments}")
  
