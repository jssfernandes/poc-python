import requests
import json
import time

from Pokemon import Pokemon

start_time = time.time()
def dict_to_class(class_name: object, dictionary: dict) -> object:
    instance = class_name()
    for key in dictionary.keys():
        setattr(instance, key, dictionary[key])
    return instance
def json_to_class(class_name: object, json_string: str) -> object:
    dict_object = json.loads(json_string)
    return dict_to_class(class_name, dict_object)

# for number in range(1, 905):
for number in range(1, 4):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = requests.get(url)
    pokemon = resp.json()
    # poke = Pokemon()
    # poke.id =pokemon['id']
    # poke.name =pokemon['name']
    # poke.height =pokemon['height']
    # poke.weight =pokemon['weight']
    # print(poke.__dict__)
    poke = dict_to_class(class_name=Pokemon, dictionary=resp.json())
    poke2 = json_to_class(class_name=Pokemon, json_string=json.dumps(resp.json()))
    # print(poke.__dict__)
    print(poke.name)
    # print(poke2.__dict__)
    print(poke2.name)

    # data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
    # x = json.loads(json.dumps(resp.json()), object_hook=lambda d: SimpleNamespace(**d))
    # print(x.name, x.id)

# x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
# print(x.name, x.hometown.name, x.hometown.id)
print("--- %s seconds ---" % (time.time() - start_time))
