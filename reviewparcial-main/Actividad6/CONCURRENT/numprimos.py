from concurrent.futures import ProcessPoolExecutor

def num_primos(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

rango = range(100000,100050)
with ProcessPoolExecutor() as executor:
  primos = list(executor.map(num_primos, rango))

print([n for n, es_primo in zip(rango, primos) if es_primo])
