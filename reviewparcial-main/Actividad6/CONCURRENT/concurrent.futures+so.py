from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess

# Definir la función que ejecutará un comando del sistema y recogerá su salida
def ejecutar_comando(comando):
    result = subprocess.run(comando, shell=True, capture_output=True, text=True)
    return result.stdout

# Lista de comandos del sistema operativo para ejecutar
comandos = [
    "echo 'Hola, mundo!'",
    "uname -a",
    "date",
    "uptime",
    "ls -l"
]

# Usar ThreadPoolExecutor para ejecutar las tareas en varios hilos
with ThreadPoolExecutor(max_workers=5) as executor:
    # Crear y enviar tareas al executor
    futures = [executor.submit(ejecutar_comando, comando) for comando in comandos]
    
    # Procesar y recolectar las salidas de los comandos
    for future in as_completed(futures):
        try:
            salida = future.result()
            print(f"Salida del comando:\n{salida}")
        except Exception as e:
            print(f"Error ejecutando el comando: {e}")

print("Todos los comandos se han ejecutado")
