#ASYNCIO 3files - 3,5,7(await)

import asyncio

async def download_file(file_name, duration):
  print(f'Iniciando la descarga de {file_name} (durará {duration} segundos)..')
  await asyncio.sleep(duration)
  print(f'Descarga completada: {file, duration} segundos')

async def main():
  await asyncio.gather(
      download_file("archivo1.txt", 3),
      download_file("archivo2.txt", 5),
      download_file("archivo3.txt", 7)
  )

# Ejecutar la función main del programa.
asyncio.run(main())
