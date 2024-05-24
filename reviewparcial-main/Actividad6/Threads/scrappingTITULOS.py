import threading
import requests
from bs4 import BeautifulSoup

# Lista de URLs para scrapear
urls = [
    'https://www.example.com',
    'https://www.python.org',
    'https://www.openai.com',
    # Añade más URLs aquí
]

def scrape_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string
    print(f"Title of {url}: {title}")

# Crear y arrancar los hilos
threads = []
for url in urls:
    thread = threading.Thread(target=scrape_title, args=(url,))
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()

print("All scraping tasks are complete.")
