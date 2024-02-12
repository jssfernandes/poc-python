import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.impute import SimpleImputer
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import FeatureUnion
# from sklearn.preprocessing import OrdinalEncoder
# from sklearn.linear_model import LinearRegression
# from pandas.plotting import scatter_matrix

# from sklearn.preprocessing import MinMaxScaler
# from sklearn.base import BaseEstimator, TransformerMixin


# import seaborn             as sns
# import missingno           as msno


import subprocess
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


df = pd.read_excel('lotofacil.xlsx')
df.head()

df.shape


# Vamos criar uma coluna para armazenar a data e converte-la para datetime
df['Data Sorteio'] = df.iloc[:,1]
df['Data Sorteio'] = pd.to_datetime(df['Data Sorteio'])

# Vamos quebrar a data em Dia, Mês e Ano
df['day']   = df['Data Sorteio'].dt.day
df['month'] = df['Data Sorteio'].dt.month
df['year']  = df['Data Sorteio'].dt.year


# Vamos criar um dataframe para analisar os sorteios que tiveram ganhadores
df_ganhadores = df[df['Acumulado 15 acertos'] == 'R$0,00']
df_ganhadores.head()


# Verificando se alguma vez as dezenas se repetiram na mesma ordem
df.groupby(['Bola1','Bola2','Bola3','Bola4','Bola5','Bola6','Bola7','Bola8','Bola9','Bola10','Bola11','Bola12','Bola13','Bola14','Bola15']).size().sort_values(ascending=False)


# As 15 dezenas mais sorteadas em todos os jogos
# 1ª Dezena	2ª Dezena	3ª Dezena	4ª Dezena ...	14ª Dezena	15ª Dezena
dezenas = pd.DataFrame(df['Bola1'].tolist() + df['Bola2'].tolist() + df['Bola3'].tolist() + df['Bola4'].tolist() + df['Bola5'].tolist() + df['Bola6'].tolist() + df['Bola7'].tolist() + df['Bola8'].tolist() + df['Bola9'].tolist() + df['Bola10'].tolist() + df['Bola11'].tolist() + df['Bola12'].tolist() + df['Bola13'].tolist() + df['Bola14'].tolist() + df['Bola15'].tolist(), columns=['numeros'])
dezenas['numeros'].value_counts().sort_values(ascending=True).head(15).plot(kind='barh', title='As quinze dezenas mais sorteadas em todos os jogos', figsize=(10,5), fontsize=12, legend=True, color='gray')


# Criando dataframe que vamos usar nos modelos
df_nn = df[['Bola1','Bola2','Bola3','Bola4','Bola5','Bola6','Bola7','Bola8','Bola9','Bola10','Bola11','Bola12','Bola13','Bola14','Bola15', 'Ganhadores 15 acertos']]

# Deixando os nomes das coluna em minusculo
df_nn.columns = map(str.lower, df_nn.columns)

df_nn.head(5)



# Pode existir mais de um ganhador por jogo
df_nn[df_nn['ganhadores 15 acertos'] >= 1].groupby('ganhadores 15 acertos')['ganhadores 15 acertos'].agg('count').plot(kind='bar',figsize=(10,5), color='gray', fontsize=12)



# Então tudo jogo que tiver mais de um ganhador deixamos como o numeor 1
df_nn.loc[df_nn['ganhadores 15 acertos'] > 1, 'ganhadores 15 acertos'] = 1
df_nn['ganhadores 15 acertos'].value_counts().plot(kind='bar', figsize=(10,5), color='gray', fontsize=12)



# print(df_nn)
features = df_nn.iloc[:,0:15]
# print(features)


dezenas_sorteadas = df[['Bola1','Bola2','Bola3','Bola4','Bola5','Bola6','Bola7','Bola8','Bola9','Bola10','Bola11','Bola12','Bola13','Bola14','Bola15']].values.tolist()
print(dezenas_sorteadas[11])