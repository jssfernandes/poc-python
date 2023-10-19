# How to merge two dicts
# in python 3.5+

x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}

z = {**x, **y}

print(z)