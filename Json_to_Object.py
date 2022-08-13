import json
class Address(object):
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __str__(self):
        return "{0} {1}".format(self.street, self.number)

class User(object):
    def __init__(self, name, address):
        self.name = name
        self.address = Address(**address)

    def __str__(self):
        return "{0} ,{1}".format(self.name, self.address)

if __name__ == '__main__':
    js = '''{"name":"Cristian", "address":{"street":"Sesame","number":122}}'''
    j = json.loads(js)
    print(j)
    u = User(**j)
    print(u)


import json
from types import SimpleNamespace

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
print(x.name, x.hometown.name, x.hometown.id)

https://pythonexamples.org/convert-python-class-object-to-json/