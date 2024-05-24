#THREADPOOLEXECUTOR FIBONACCI

from concurrent.futures import ThreadPoolExecutor

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

entradas = [10, 20, 30, 35, 40]

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(fibonacci, entrada) for entrada in entradas]

    for future in futures:
        print(f"Resultado del cálculo de Fibonacci: {future.result()}")

print("Todos los cálculos de Fibonacci han finalizado")
