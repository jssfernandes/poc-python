import pandas as pd
import subprocess
import time

tempo_inicial = time.time()

teste=[[1,3,5,7,9,10,11,13,14,17,19,20,21,22,25,],[1,2,3,5,7,9,10,11,13,14,17,19,21,22,25,],[1,2,3,4,5,7,9,10,11,12,13,14,17,19,20,21,22,23,24,25,],[1,4,5,6,7,9,11,12,13,17,19,20,21,24,25,],[1,3,5,6,7,9,12,13,15,17,19,21,23,24,25,],[1,2,4,5,6,8,11,13,15,16,17,18,21,22,25,],[1,3,5,7,9,10,12,14,16,17,19,20,22,23,25,],[1,3,4,6,7,8,9,11,13,16,17,19,21,24,25,],[2,3,4,6,7,9,11,13,14,15,17,19,21,22,24,],[2,3,4,6,7,9,11,13,14,15,17,19,21,22,24,],[1,2,3,6,9,10,12,13,17,18,19,21,22,24,25,],[2,3,4,6,7,9,11,13,14,15,17,19,21,22,24,],[2,3,4,7,8,10,13,15,16,18,19,21,23,24,25,],[2,5,6,7,8,9,10,13,15,16,19,20,23,24,25,],[1,4,5,8,9,11,13,14,16,19,20,21,22,24,25,],[1,3,4,5,6,8,9,12,13,14,17,20,21,22,25,],[2,3,5,6,7,8,9,13,14,15,16,18,19,21,23,],[1,2,4,5,6,8,11,13,14,15,16,18,20,23,25,],[1,2,3,5,7,9,11,13,15,17,18,22,23,24,25,],[1,3,5,7,9,10,11,13,14,17,19,20,21,22,25,],[1,2,3,5,7,9,10,11,13,14,17,19,21,22,25,],[1,4,5,6,7,9,11,12,13,17,19,20,21,24,25,],[1,3,5,6,7,9,12,13,15,17,19,21,23,24,25,],[1,2,4,5,6,8,11,13,15,16,17,18,21,22,25,],[1,3,5,7,9,10,12,14,16,17,19,20,22,23,25,],[1,3,4,6,7,8,9,11,13,16,17,19,21,24,25,],[2,3,4,6,7,9,11,13,14,15,17,19,21,22,24,],[1,2,3,6,9,10,12,13,17,18,19,21,22,24,25,],[1,2,3,6,9,10,12,13,17,18,19,21,22,24,25,],]
meus_numeros = [
[1,3,5,7,9,10,11,13,14,17,19,20,21,22,25,],
[1,2,3,5,7,9,10,11,13,14,17,19,21,22,25,],
[1,2,3,4,5,7,9,10,11,12,13,14,17,19,20,21,22,23,24,25,],
[1,4,5,6,7,9,11,12,13,17,19,20,21,24,25,],
[1,3,5,6,7,9,12,13,15,17,19,21,23,24,25,],
[1,2,4,5,6,8,11,13,15,16,17,18,21,22,25,],
[1,3,5,7,9,10,12,14,16,17,19,20,22,23,25,],
[1,3,4,6,7,8,9,11,13,16,17,19,21,24,25,],
[2,3,4,6,7,9,11,13,14,15,17,19,21,22,24,],
[1,2,3,6,9,10,12,13,17,18,19,21,22,24,25,],
[2,3,4,7,8,10,13,15,16,18,19,21,23,24,25,],
[2,5,6,7,8,9,10,13,15,16,19,20,23,24,25,],
[1,4,5,8,9,11,13,14,16,19,20,21,22,24,25,],
[1,3,4,5,6,8,9,12,13,14,17,20,21,22,25,],
[2,3,5,6,7,8,9,13,14,15,16,18,19,21,23,],
[1,2,4,5,6,8,11,13,14,15,16,18,20,23,25,],
[1,2,3,5,7,9,11,13,15,17,18,22,23,24,25,],
[1,3,5,6,7,9,12,13,15,17,19,21,23,24,25,],
[1,2,4,5,6,8,9,11,13,15,17,19,20,21,23,24,],
]
# print(len(teste))
# result=[]
# for i in teste:
#     if i not in result:
#         result.append(i)
# print(len(result))
# print(len(meus_numeros))


def curl_request(url):
    # Define the command to execute using curl
    command = ['curl', '-k', url, '-o','lotofacil.xlsx']
    # Execute the curl command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)
    # print(result)
    # Return the stdout of the curl command
    return result.stdout
# Make a curl request to https://www.google.com/
response = curl_request('https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Lotof%C3%A1cil')
# Make a curl request to https://www.google.com/
# print(response)

def estatistica_dos_resultados(dezenas_sorteadas, numeros_apostado):
    acertos_11 = 0
    acertos_12 = 0
    acertos_13 = 0
    acertos_14 = 0
    acertos_15 = 0
    for i in dezenas_sorteadas:
        dezenas_acertadas = list(set(numeros_apostado) & set(i[0:15]))
        # print(len(dezenas_acertadas))
        
        #print(dezenas_acertadas)
        if len(dezenas_acertadas) == 11:
            acertos_11 = acertos_11 + 1
        if len(dezenas_acertadas) == 12:
            acertos_12 = acertos_12 + 1
        if len(dezenas_acertadas) == 13:
            acertos_13 = acertos_13 + 1
        if len(dezenas_acertadas) == 14:
            acertos_14 = acertos_14 + 1
        if len(dezenas_acertadas) == 15:
            #print(len(dezenas_acertadas))
            #print(dezenas_acertadas)
            #print(i[0:15])
            acertos_15 = acertos_15 + 1
    retorno = {}
    if len(dezenas_sorteadas) > 1:
        retorno = {
        "numeros apostados": numeros_apostado,
        "quantidade dezenas": len(numeros_apostado),
        "15 acertos": acertos_15,
        "14 acertos": acertos_14,
        "13 acertos": acertos_13,
        "12 acertos": acertos_12,
        "11 acertos": acertos_11,
    }
    else:
        retorno = {
        "numeros apostados": numeros_apostado,
        "quantidade dezenas": len(numeros_apostado),
        "15 acertos": acertos_15,
        "14 acertos": acertos_14,
        "13 acertos": acertos_13,
        "12 acertos": acertos_12,
        "11 acertos": acertos_11,
        "quantidade de acertos": len(dezenas_acertadas),
    }
    return retorno

df = pd.read_excel('lotofacil.xlsx')
'''
print(df.head())

print(df.shape)
'''


# Vamos criar uma coluna para armazenar a data e converte-la para datetime
df['Data Sorteio'] = df.iloc[:,1]
df['Data Sorteio'] = pd.to_datetime(df['Data Sorteio'])

# Vamos quebrar a data em Dia, Mês e Ano
df['day']   = df['Data Sorteio'].dt.day
df['month'] = df['Data Sorteio'].dt.month
df['year']  = df['Data Sorteio'].dt.year


# Verificando se alguma vez as dezenas se repetiram na mesma ordem
df.groupby(['Bola1','Bola2','Bola3','Bola4','Bola5','Bola6','Bola7','Bola8','Bola9','Bola10','Bola11','Bola12','Bola13','Bola14','Bola15']).size().sort_values(ascending=False)

# dezenas_sorteadas = df[['Bola1','Bola2','Bola3','Bola4','Bola5','Bola6','Bola7','Bola8','Bola9','Bola10','Bola11','Bola12','Bola13','Bola14','Bola15']].values.tolist()
dezenas_sorteadas_data = df[['Bola1','Bola2','Bola3','Bola4','Bola5','Bola6','Bola7','Bola8','Bola9','Bola10','Bola11','Bola12','Bola13','Bola14','Bola15', 'Data Sorteio']].values.tolist()
# print(dezenas_sorteadas[11])

# # As 15 dezenas mais sorteadas em todos os jogos
# # 1ª Dezena	2ª Dezena	3ª Dezena	4ª Dezena ...	14ª Dezena	15ª Dezena
# dezenas = pd.DataFrame(df['Bola1'].tolist() + df['Bola2'].tolist() + df['Bola3'].tolist() + df['Bola4'].tolist() + df['Bola5'].tolist() + df['Bola6'].tolist() + df['Bola7'].tolist() + df['Bola8'].tolist() + df['Bola9'].tolist() + df['Bola10'].tolist() + df['Bola11'].tolist() + df['Bola12'].tolist() + df['Bola13'].tolist() + df['Bola14'].tolist() + df['Bola15'].tolist(), columns=['numeros'])
# # dezenas['numeros'].value_counts().sort_values(ascending=True).head(15).plot(kind='barh', title='As quinze dezenas mais sorteadas em todos os jogos', figsize=(10,5), fontsize=12, legend=True, color='gray')
# # dezenas['numeros'].value_counts().sort_values(ascending=False)
# dezenas['numeros'].value_counts().sort_values(ascending=False).head(15)

sorteados = []
meus_numeros.append([1, 4, 5, 7, 9, 10, 12, 14, 15, 16, 18, 19, 21, 22, 24])
meus_numeros.append([1, 2, 5, 6, 7, 8, 9, 10, 11, 13, 15, 18, 20, 22, 24])


meus_numeros.append([2,3,5,7,8,10,13,14,15,16,17,18,19,22,25]) # numeros do sorteio dia 25/08/2023
meus_numeros.append([1,3,4,5,6,7,10,11,14,18,19,20,23,24,25]) # numeros do sorteio dia 09/09/2023
# for i in meus_numeros:
#     if i in dezenas_sorteadas:
#         print('foi sorteado alguma vez os 15 numeros')
#         print(i)
#         sorteados.append(i)
# if not sorteados:
#     print('nao foi dessa vez')
#print(dezenas_sorteadas_data)
'''
for i in dezenas_sorteadas_data:
    if i[0:15] in meus_numeros:
        print('foi sorteado alguma vez os 15 numeros')
        print(i)
        sorteados.append(i)

if not sorteados:
    print('nao foi dessa vez')
'''
# for i in dezenas_sorteadas:
#     if i in sorteados:
#         print('foi sorteado alguma vez os 15 numeros')
#         print(i)


# # for i in meus_numeros:
# #     print(i)
# #     if i in dezenas_sorteadas:

# for i in dezenas_sorteadas:
#     # print(i)
#     if i == meus_numeros[1]:
#         print('foi sorteado alguma vez os 15 numeros')
#         print(i['Data Sorteio'])

'''
for i in meus_numeros:
    print()
    print(estatistica_dos_resultados(dezenas_sorteadas_data, i))
'''
    

aposta = [1,3,5,6,7,9,12,13,15,17,19,21,23,24,25,]
print()
print('Acertos do ultimo sorteio')
print('Data do sorteio', dezenas_sorteadas_data[-1][-1])
print(estatistica_dos_resultados([dezenas_sorteadas_data[-1]], aposta))
print()
print('Estatisticas de todos os sorteios')
print(estatistica_dos_resultados(dezenas_sorteadas_data, aposta))

#estatistica_dos_resultados(dezenas_sorteadas_data, meus_numeros[1])
tempo_final = time.time()
print()
print(f"Dutação foi de {tempo_final-tempo_inicial} segundos")

