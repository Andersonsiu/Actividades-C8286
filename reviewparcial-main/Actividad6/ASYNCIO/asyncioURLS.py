#ASYNC URLS (AIOHTTP)

import asyncio
import aiohttp

urls = ['https://www.instagram.com/melbet_peru/', 'https://www.instagram.com/tus20fijas/', 'https://www.instagram.com/realmadrid/']

async def download_url(session,url):
  async with session.get(url) as response:
    content = await response.text()
    print(f'Descargado {url}: {len(content)} bytes')

async def main():
  async with aiohttp.ClientSession() as session:
    tasks = [download_url(session,url) for url in urls]
    await asyncio.gather(*tasks)
