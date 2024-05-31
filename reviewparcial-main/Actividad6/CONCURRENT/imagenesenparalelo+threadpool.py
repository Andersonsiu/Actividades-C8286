from concurrent.futures import ThreadPoolExecutor
import requests
import os

# Definir la función que descargará una imagen desde una URL y la guardará en el disco
def descargar_imagen(url, nombre_archivo):
    response = requests.get(url)
    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as file:
            file.write(response.content)
        print(f"Imagen guardada como {nombre_archivo}")
    else:
        print(f"Error al descargar la imagen desde {url}")

# Lista de URLs de imágenes
urls = [
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5_tQxA2uRMfXoVQK7LTGfl-QNFpoukVTnEBm2zgXXaw&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGI4AzKqU5Zaj2qp2TCK6yx1_5CObNzy-DIrBRRS4G8w&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqqCUXwoHnI5GVkK8GB5zGLXI6ymDTleb_i6bT2u77Dw&s',
    'https://ichef.bbci.co.uk/ace/ws/640/cpsprodpb/10413/production/_100697566_hi045932006.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDcawUB_obz66XTb72Ch1cKSOR4V0WJ0KVh8ucwZCJ6Q&s'
]

# Usar ThreadPoolExecutor para descargar las imágenes en paralelo
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = []
    for i, url in enumerate(urls):
        nombre_archivo = f"imagen_{i + 1}.jpg"
        futures.append(executor.submit(descargar_imagen, url, nombre_archivo))

    # Esperar a que todas las tareas se completen
    for future in futures:
        future.result()

print("Todas las imágenes se han descargado")
