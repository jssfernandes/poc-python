def vogal(letra):
    vogais = "aeiou"
    if letra.lower() not in vogais: # verificar se a letra digitada minuscula nao existe na nossa variavel vogais
        return False
    return True

letra = input("Digite uma letra: ")
print(vogal(letra)) # aqui imprime True ou False

def vogal_opcao_2(z):
    vogais = ['a', 'e', 'i', 'o', 'u']
    return z.lower() in vogais

