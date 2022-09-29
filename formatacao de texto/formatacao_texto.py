##### Variáveis em texto - foramtacao simples #####
valor = 1000

print(f"Faturamento: {valor}")


##### leitura arquivo #####
# nome_arquivo = "pessoas.txt"
# caminho_win = r'C:\Users\UserName\Documents'
# arquivo = open(f"{caminho_win}/{nome_arquivo}", "r")
# caminho_lin = r'/home/UserName/Documents'
# arquivo = open(f"{caminho_lin}/{nome_arquivo}", "r")
# print(arquivo.read())
# arquivo.close()


##### Formatando com casa decimal #####
print(f"Faturamento: {valor:.2f}")


##### Formato Moeda #####
print(f"Faturamento: R${valor:,.2f}")


##### Número fixo de dígitos #####
cpf = 11233344
print(f"CPF: {cpf:011}")


##### Percentual #####
desconto = 0.17

print(f"Margem: {desconto:.1%}")


##### Datas #####
from datetime import datetime

hoje = datetime.now()
print(f"Data: {hoje:%d/%m/%Y}, Horário: {hoje:%H:%M}")


##### Cuidado com textos com chaves {} #####
produto = 'Placa mãe'
print(f"{{Produto: {produto}}}")


##### Campo de texto texto #####
texto = f"""Bom dia, 

Produto: {produto}
Valor Produto: R${valor:,.2f}
Desconto a Vista: {desconto:.1%}
Data de hoje: {hoje:%d/%m/%Y}
"""
print(texto)
