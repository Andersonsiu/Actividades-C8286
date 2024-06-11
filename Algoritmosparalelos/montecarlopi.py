import multiprocessing as mp
import random
import time

#n = numero de puntos a generar
def monte_carlo_pi_part(n):
  #almacenar num puntos dentro del circulo
    count = 0
    #bucle genera puntos aleatorios (x,y) en rango (0:1]
    for _ in range(n):
        x, y = random.random(), random.random() #coordenadas x, y
        #verifica si el punto esta dentro del circulo de radio 1
        if x**2 + y**2 <= 1.0:
            count += 1
    #retorna num puntos dentro del ciruclo
    return count

#distribuye carga de trabajo entre multiples procesos
def parallel_monte_carlo_pi(total_samples, num_processes):
    #pool de procesos
    pool = mp.Pool(processes=num_processes)
    #crea una lista en la que cada elemento representa el número de muestras que cada proceso manejará.
    samples_per_process = [total_samples // num_processes] * num_processes
    #asigna cada proceso una parte de los puntos totales para generar y contar los puntos totales
    counts = pool.map(monte_carlo_pi_part, samples_per_process)
    #se estima n sumando los puntos dentro del circulo
    pi_estimate = sum(counts) / total_samples * 4 #formula a.circulo dentro de un cuadrado
    return pi_estimate

if __name__ == "__main__":
    total_samples = 10**7
    num_processes = 4

    start_time = time.time()
    #calcula n usando paralallel
    pi_estimate = parallel_monte_carlo_pi(total_samples, num_processes)
    end_time = time.time()

    print(f"Pi estimado: {pi_estimate}")
    print(f"Tiempo tomado: {end_time - start_time} en segundos")
