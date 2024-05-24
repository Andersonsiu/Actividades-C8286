#THREADPOOLEXECUTOR + SUMA
#EJER4
from concurrent.futures import ThreadPoolExecutor

def sum_range(start,end):
  return sum(range(start,end+1))

ranges = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

with ThreadPoolExecutor(max_workers=5) as executor:
  futures = [executor.submit(sum_range, start, end) for start, end in ranges]

  for future in futures:
    print(f'Resultado de la suma {future.result()}')
  
print(f'Todos los calculos de suma finalizaron')
