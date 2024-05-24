#multiprocessing factorial paralela 5,7,9

from multiprocessing import Process
import math

def calculate_factorial(number):
    result = math.factorial(number)
    print(f"El factorial de {number} es {result}")


numbers = [5, 7, 9]
processes = []


for number in numbers:
    process = Process(target=calculate_factorial, args=(number,))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

print("Todos los cálculos de factorial han finalizado")
