from multiprocessing import Pool
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

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        titles = pool.map(scrape_title, urls)
        for title in titles:
            print(title)

    print("All scraping tasks are complete.")
