# Expressões Lambda - Simplificado
# Funções "Anônimas" -> nome ruim pra uma função que você não precisa definir e depois usar, você define já usando direto.
# Ex:
# Digamos que você está avaliando o preço de um serviço e quer saber quanto de imposto será cobrado sobre o serviço. O imposto é correspondente a 30% do valor do produto
preco = 5

# função normal
def calcular_imposto(preco):
    return preco * 0.3
print(calcular_imposto(preco))

# função lambda
calcular_imposto2 = lambda x: x*0.3
print(calcular_imposto2(preco))


# Tá, mas qual a diferença?
# Quando você aplica essa função dentro de outros métodos do Python. Aí sim existe vantagem.
# Ex: temos agora uma lista de preços.
precos = [100, 500, 10, 25]

# a funcao map() por padrao recebe dois argumentos, uma funcao e uma lista, dessa lista ela executa uma iteração e recebe os resultados da funcão passada no argumento
impostos = list(map(lambda x: x*0.3, precos))
print(impostos)