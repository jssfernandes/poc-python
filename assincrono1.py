##################### Assicrono #####################
import requests
import time

start_time = time.time()

for number in range(1, 905):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = requests.get(url, verify=False)
    pokemon = resp.json()
    print(pokemon['name'])

print("--- %s seconds ---" % (time.time() - start_time))
