import requests
import json
from pokemon import Pokemon


pokemons = []
for number in range(1, 152):
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


# Exemplo 2: Converter propriedades do objeto de classe Python em string JSON
# Neste exemplo, definiremos uma classe Python com diferentes tipos de dados como string, int e float, também foi incluido um ordenador e uma identação para exibir um print mais amigavel.

#convert to JSON string
jsonStr = json.dumps(pokemons[1].__dict__, sort_keys=True, indent=4)

#print json string
print(jsonStr)
