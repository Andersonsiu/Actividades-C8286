from concurrent.futures import ThreadPoolExecutor
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
    return f"Title of {url}: {soup.title.string}"

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(scrape_title, url) for url in urls]
    for future in concurrent.futures.as_completed(futures):
        print(future.result())

print("All scraping tasks are complete.")
