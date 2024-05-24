#DESCARGAR CONTENIDO URL WITH THREADS AND REQUESTS

import threading
import requests

urls = [
    'http://www.example.com',
    'http://www.python.org',
    'http://www.openai.com',
]

def download_url(url):
    response = requests.get(url)
    print(f"Downloaded {url}: {len(response.content)} bytes")

# Crear y arrancar hilos
threads = []
for url in urls:
    thread = threading.Thread(target=download_url, args=(url,))
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()

print("All downloads complete.")
