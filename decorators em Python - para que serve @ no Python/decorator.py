# Para que serve um decorator no Python?
# Ele vai atribuir uma nova funcionalidade para a função que está logo abaixo a ele. 
# Ele nada mais é do que uma função que atribui uma nova funcionalidade para outra função.


import requests
import time

# Nesse exemplo criamos um decorator para calcular o tempo que uma função é executada.
def calcular_tempo(funcao):
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()
        print(f"Dutação foi de {tempo_final-tempo_inicial} segundos")
    return wrapper

# Aqui nós estamos utilizando esse código para obter a cotação do dólar, mas estamos criando o nosso decorator que vai calcular o tempo de execução do nosso código.
# Então sempre que você colocar o decorator @calcular_tempo ele vai funcionar como colocamos na função, então vai calcular o tempo inicial, vai rodar a função e depois vai calcular o tempo final.
# Dessa forma podemos subtrair o tempo final do inicial para saber o tempo de execução da função.
@calcular_tempo
def pegar_cotacao_dolar():
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])

pegar_cotacao_dolar()