#################### Assicrono ####################
import aiohttp
import asyncio
import time
import sys

if sys.platform:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

start_time = time.time()


async def main():
    async with aiohttp.ClientSession() as session:
        for number in range(1, 905):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                print(pokemon['name'])


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
