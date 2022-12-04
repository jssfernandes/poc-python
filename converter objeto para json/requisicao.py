import requests
import json
from pokemon import Pokemon


pokemons = []
for number in range(1, 2):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    response = requests.get(url)

    pokemon_json = response.json()
    pokemon_class = Pokemon(**pokemon_json)
    pokemons.append(pokemon_class)

# Exemplo 1: Converter objeto de classe Python em string JSON
# Neste exemplo, definiremos uma classe Python, criaremos um objeto para a classe python e depois converteremos suas propriedades em uma string JSON.
jsonStr = json.dumps(pokemons[0].__dict__)

#print json string
print(jsonStr)
print()


