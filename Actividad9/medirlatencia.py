import time
import numpy as np

def measure_latency(array_size):
    array = np.zeros(array_size)
    start_time = time.perf_counter()
    
    # Acceder a todos los elementos del array
    for i in range(array_size):
        array[i] += 1
    
    end_time = time.perf_counter()
    latency = end_time - start_time
    return latency

sizes = [10**3, 10**4, 10**5, 10**6, 10**7]
latencies = []

for size in sizes:
    latency = measure_latency(size)
    latencies.append(latency)
    print(f"Tamaño del array: {size}, Latencia: {latency:.6f} segundos")

# Graficar los resultados
import matplotlib.pyplot as plt

plt.plot(sizes, latencies, marker='o')
plt.xlabel('Tamaño del Array')
plt.ylabel('Latencia (segundos)')
plt.xscale('log')
plt.yscale('log')
plt.title('Latencia de Acceso a Datos en Diferentes Tamaños de Array')
plt.show()
