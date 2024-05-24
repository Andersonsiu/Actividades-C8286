import threading

contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(100000):
        with lock:
            contador += 1

# Crear y arrancar los hilos
hilos = []
for _ in range(5):
    hilo = threading.Thread(target=incrementar)
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print(f"Valor final del contador: {contador}")
