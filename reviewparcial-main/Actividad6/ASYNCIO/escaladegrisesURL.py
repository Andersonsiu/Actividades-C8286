import asyncio
import aiohttp
from PIL import Image
from io import BytesIO
import os

# Función asíncrona para descargar una imagen desde una URL
async def descargar_imagen(url, session, nombre_archivo):
    async with session.get(url) as response:
        if response.status_code == 200:
            contenido = await response.read()
            with open(nombre_archivo, 'wb') as file:
                file.write(contenido)
            return nombre_archivo
        else:
            print(f"Error al descargar la imagen desde {url}")
            return None

# Función para procesar la imagen (convertir a escala de grises)
def procesar_imagen(nombre_archivo):
    with Image.open(nombre_archivo) as img:
        img_gris = img.convert("L")
        nombre_procesado = f"procesado_{os.path.basename(nombre_archivo)}"
        img_gris.save(nombre_procesado)
        print(f"Imagen procesada guardada como {nombre_procesado}")
        return nombre_procesado

# Función principal para gestionar las descargas y el procesamiento
async def main():
    urls = [
        'https://www.example.com/image1.jpg',
        'https://www.example.com/image2.jpg',
        'https://www.example.com/image3.jpg',
        'https://www.example.com/image4.jpg',
        'https://www.example.com/image5.jpg'
    ]

    # Crear una sesión de aiohttp
    async with aiohttp.ClientSession() as session:
        # Crear tareas para descargar las imágenes
        tareas_descarga = [descargar_imagen(url, session, f"imagen_{i + 1}.jpg") for i, url in enumerate(urls)]
        
        # Esperar a que todas las descargas se completen
        archivos_descargados = await asyncio.gather(*tareas_descarga)

    # Filtrar las descargas exitosas
    archivos_descargados = [archivo for archivo in archivos_descargados if archivo is not None]

    # Procesar las imágenes descargadas en paralelo utilizando asyncio
    loop = asyncio.get_event_loop()
    tareas_procesamiento = [loop.run_in_executor(None, procesar_imagen, archivo) for archivo in archivos_descargados]
    
    # Esperar a que todos los procesamientos se completen
    archivos_procesados = await asyncio.gather(*tareas_procesamiento)

    print("Todas las imágenes se han descargado y procesado")

# Ejecutar la función principal
asyncio.run(main())
