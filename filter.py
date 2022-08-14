# uma lista contendo numeros
seq = [0, 1, 2, 3, 5, 8, 13, 21]

# filtrando numeros pares
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# filtrando numeros impares
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))

# filtrando numeros um numero qualquer
result = filter(lambda x: x == 8, seq)
print(list(result))
