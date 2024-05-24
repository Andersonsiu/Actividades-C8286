import asyncio
import aiohttp


async def fetch(url,session):
    async with session.get(url) as response:
        print(f'Status:{response.status}')
        data = await response.text()
        print(f'Data from {url} feteched')
        return data


async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url,session) for url in urls]
        await asyncio.gather(*tasks)


urls = ['https://en.wikipedia.org/wiki/Cristiano_Ronaldo']*5
asyncio.run(main(urls))
