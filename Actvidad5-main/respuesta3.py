import concurrent.futures
import time

# Función que simula una tarea que puede fallar o tardar mucho
def task(id, duration):
    try:
        print(f"Iniciando tarea {id} que tardará {duration} segundos.")
        time.sleep(duration)  # Simula tiempo de procesamiento
        print(f"Tarea {id} completada.")
        return f"Resultado de la tarea {id}"
    except Exception as e:
        return f"Tarea {id} falló: {str(e)}"

# Función principal que ejecuta tareas utilizando un Bulkhead
def main():
    # Usar ThreadPoolExecutor como un Bulkhead
    # Limitamos el número de tareas simultáneas a 3
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Simulamos la recepción de tareas con diferentes duraciones
        tasks = {executor.submit(task, i, duration): i for i, duration in enumerate([2, 3, 5, 1, 4])}
        for future in concurrent.futures.as_completed(tasks):
            task_id = tasks[future]
            try:
                result = future.result()
                print(f"Tarea {task_id} completada con resultado: {result}")
            except Exception as e:
                print(f"Tarea {task_id} generó una excepción: {str(e)}")

if __name__ == "__main__":
    main()
