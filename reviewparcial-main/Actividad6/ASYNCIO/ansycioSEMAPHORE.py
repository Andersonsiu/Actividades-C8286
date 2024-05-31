import ansycio

semaforo = asyncio.Semaphore(3)

async def tarea(numero):
  async with semaforo:
    print(f'Tarea {numero} esta accediendo al recurso')
    await asyncio.sleep(2)
    print(f'Tarea {numero} ha liberado el recuerso')

async def main():
  tareas = [asyncio.create_task(tarea(i)) for i in range(10)]
  await asyncio.gather(*tareas)

asyncio.run(mai())
