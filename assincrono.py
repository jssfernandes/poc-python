##################### Sicrono #####################
# How do I disable the security certificate check in Python requests
# https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests

import requests
import time

start_time = time.time()

for number in range(1, 905):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = requests.get(url)
    pokemon = resp.json()
    print(pokemon['name'])

print("--- %s seconds ---" % (time.time() - start_time))

#################### Assicrono ####################
# how can I ignore the SL error of asyncio in python?
# https://stackoverflow.com/questions/53471957/how-can-i-ignore-the-sl-error-of-asyncio-in-python
"""
Navigate to
cd /Applications/Python\ 3.7/

Click on Install Certificates.command

This should solve it.
"""
"""
Better with certifi module:

import ssl
import certifi

sslcontext = ssl.create_default_context(cafile=certifi.where())
with aiohttp.Timeout(10):
        ......
        async with session.get(url, ssl=sslcontext) as response:
            ......
"""
import aiohttp
import asyncio
import sys

if sys.platform:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    async with aiohttp.ClientSession() as session:
        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
        async with session.get(pokemon_url) as resp:
            pokemon = await resp.json()
            print(pokemon['name'])


asyncio.run(main())

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

#################### Assicrono ####################
import aiohttp
import asyncio
import time
import sys

if sys.platform:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

start_time = time.time()


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name']


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1, 905):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
