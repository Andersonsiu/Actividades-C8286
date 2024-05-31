### sleep.py

import asyncio

async def lazy_printer(delay, message):
    await asyncio.sleep(delay)
    print(message)

asyncio.wait([lazy_printer(1, 'Lento'), lazy_printer(0, 'Full velocidad')])
#asyncio.run()