#Concurrent.futures WITH ThreadPoolExecutor, ProcessPoolExecutor
#SUMA DE NUMEROS

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

list_of_numbers = [list(range(100000)), list(range(100000, 200000)), list(range(200000, 300000)), list(range(300000, 400000))]

def sum_numbers(numbers):
  return sum(numbers)

#THREADPOOLEXECUTOR
with ThreadPoolExecutor() as executor:
  results = executor.map(sum_numbers, list_of_numbers)
  for result in results:
    print(f'Suma Threads: {result}')

#PROCESSPOOLEXECUTOR

with ProcessPoolExecutor() as executor:
  results = executor.map(sum_numbers, list_of_numbers)
  for result in results:
    print(f'Suma Process: {result}')
