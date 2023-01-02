carros = [
    {"modelo": "Mustang GT 500", "marca": "Ford"},
    {"modelo": "Pontiac GTO", "marca": "Pontiac"},
    {"modelo": "Chevelle", "marca": "Chevrolet"},
    {"modelo": "Challenger", "marca": "Dodge"},
    {"modelo": "Zonda C12", "marca": "Pagani"},
]

# para ordenar quando se contem um dicionario é necessario uma funcao para fazer algun filtro por um campo em especifico do dicionario
# ordenacao por modelo
carros.sort(key=lambda carros: carros["modelo"])
print("\nLista ordenada por modelo")
print(carros)

# ordenacao por marca
carros.sort(key=lambda carros: carros["marca"])
print("\nLista ordenada por marca")
print(carros)