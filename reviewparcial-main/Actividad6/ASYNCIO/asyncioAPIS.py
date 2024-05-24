import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
  urls = [
        'https://api.chucknorris.io/jokes/random',
        'https://api.coindesk.com/v1/bpi/currentprice.json',
        'https://dog.ceo/api/breeds/image/random'
  ]
  tasks = [fetch(url) for url in urls]
  responses = await asyncio.gather(*tasks)

  for i, response in enumerate(responses):
    print(f"Respuesta de la API {i + 1}:\n{response}\n")

# Ejecutar la función principal
asyncio.run(main())
