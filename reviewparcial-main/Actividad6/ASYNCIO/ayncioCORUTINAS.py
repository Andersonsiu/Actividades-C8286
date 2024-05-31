#RELOJ IN 10s
import asyncio

async def clock():
  for second in range(1,11):
    print(f'Han pasado {second} segundos')
    await asyncio.sleep(1)

asyncio.run(main())
