from multiprocessing import Process, Queue

def calcular_cuadrado(num, queue):
    queue.put(num ** 2)

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]
    queue = Queue()
    procesos = []

    for num in numeros:
        p = Process(target=calcular_cuadrado, args=(num, queue))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    while not queue.empty():
        print(queue.get())
