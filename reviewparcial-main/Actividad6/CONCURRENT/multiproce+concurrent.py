import concurrent.futures
import multiprocessing
import pandas as pd
import numpy as np

def analyze_data(data_chunk):
    """Función que realiza cálculos estadísticos en un fragmento de datos."""
    result = {
        'mean': np.mean(data_chunk),
        'std_dev': np.std(data_chunk),
        'max': np.max(data_chunk),
        'min': np.min(data_chunk)
    }
    return result

def data_distributor(data, num_workers):
    """Distribuye los datos en fragmentos para cada trabajador."""
    chunk_size = len(data) // num_workers
    return (data[i * chunk_size:(i + 1) * chunk_size] for i in range(num_workers))

def main():
    # Simulando algunos datos grandes
    data = np.random.randn(10000)  # 10,000 puntos de datos aleatorios
    
    num_workers = multiprocessing.cpu_count()  # Número de procesos a utilizar
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
        # Distribuir datos
        chunks = data_distributor(data, num_workers)
        
        # Ejecutar análisis en paralelo
        results = list(executor.map(analyze_data, chunks))
        
        # Procesar y combinar resultados
        final_report = pd.DataFrame(results)
        print("Reporte final:")
        print(final_report.describe())  # Genera un reporte estadístico del resumen de resultados

if __name__ == "__main__":
    main()
