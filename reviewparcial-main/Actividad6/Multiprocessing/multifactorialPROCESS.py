#multiprocessing factorial with Process

from multiprocessing import Process
import math

numbers = [100000, 100050, 100100, 100150]

def calculate_factorial(n):
    print(f"Factorial of {n}: {math.factorial(n)}")

# Crear y arrancar procesos
processes = []
for number in numbers:
    process = Process(target=calculate_factorial, args=(number,))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

print("All factorial calculations complete.")
