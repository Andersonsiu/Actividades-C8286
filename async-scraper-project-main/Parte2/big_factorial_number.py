import multiprocessing
import math
import sys
sys.set_int_max_str_digits(0)

def calcular_factorial(numero):
    resultado = math.factorial(numero)
    print(f"El factorial de {numero} es {resultado}")
    return resultado

#lista de numeros grandes
numeros = [100000 + x for x in range(5)] #LIsta de cinco numeros grandes

if __name__ == '__main__':
    with multiprocessing.Pool(processes=5) as pool:
        resultados = pool.map(calcular_factorial, numeros)
    print("Resultados:", resultados)

