# https://docs.python.org/3/library/logging.html#logrecord-attributes

import logging

# Configurando e salvando o log em um arquivo
logging.basicConfig(level=logging.INFO, filename="programa.log", format="%(asctime)s - %(levelname)s - %(message)s")

def resultado_operacional(faturamento, custo):
    return faturamento - custo

def lucro_liquido(faturamento, custo, percentual_imposto):
    if percentual_imposto == 0:
        logging.warning("Percentual de imposto é 0")
    return (faturamento - custo) * (1 - percentual_imposto)

def lucro_por_acoes(faturamento, custo, percentual_imposto, acoes):
    if acoes == 0:
        logging.error("Ações não pode ser igual a 0")
    return lucro_liquido(faturamento, custo, percentual_imposto) / acoes


faturamento = 1000
custo = 400
percentual_imposto = 0.3
acoes = 0


resultado = resultado_operacional(faturamento, custo)
logging.info(f"Resultado: {resultado}")

lucro = lucro_liquido(faturamento, custo, percentual_imposto)
logging.info(f"Lucro: {lucro}")

lucro_acao = lucro_por_acoes(faturamento, custo, percentual_imposto, acoes)
logging.info(f"Lucro por ação: {lucro_acao}")


# #### Resumo:
#
# logging.debug
# DEBUG - Informação detalhada, tipicamente de interesse apenas quando diagnosticando problemas.
#
# logging.info
# INFO - Confirmação de que as coisas estão funcionando como esperado.
#
# logging.warning
# WARNING - Uma indicação que algo inesperado aconteceu, ou um indicativo que algum problema em um futuro próximo (ex.: ‘pouco espaço em disco’). O software está ainda funcionando como esperado.
#
# logging.error
# ERROR - Por conta de um problema mais grave, o software não conseguiu executar alguma função.
#
# logging.critical
# CRITICAL - Um erro grave, indicando que o programa pode não conseguir continuar rodando.
