import requests
from pokemon import Pokemon


pokemons = []
for number in range(1, 152):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    response = requests.get(url)

    pokemon_json = response.json()
    pokemon_class = Pokemon(**pokemon_json)
    pokemons.append(pokemon_class)

for pokemon in pokemons:
    print(pokemon.id)
    print(pokemon.name)
    print(pokemon.types)


