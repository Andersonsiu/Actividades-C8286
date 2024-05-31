from multiprocessing import Pool
import math

def squared_number(n):
  return n*n

numbers = list(range(1,11))

if __name__ == '__main__':
  with Pool(processes=4) as pool:
    results = pool.map(squared_number, numbers)
    print(results)
