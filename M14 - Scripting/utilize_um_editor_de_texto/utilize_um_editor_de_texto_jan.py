# Importando as bibliotecas

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Função para criar os gráficos

def analise_sinasc_janeiro_2019(df, value, index, aggfunc, ylabel, xlabel, opcao='nada'):
   if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index, aggfunc=aggfunc).plot(figsize=[15, 5])
   elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index, aggfunc=aggfunc).sort_values(value).plot(figsize=[15, 5])
   elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index, aggfunc=aggfunc).unstack().plot(figsize=[15, 5])

   plt.ylabel(ylabel)
   plt.xlabel(xlabel)

   return None

# Lendo o dataframe

df_janeiro = pd.read_csv('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/SINASC_RO_2019_JAN.csv')

# Criando um diretório apenas para o mês de janeiro

max_data = df_janeiro.DTNASC.max()[:7]
max_data
os.makedirs('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/' + max_data, exist_ok=True)

# Criando os gráficos e salvando-os na pasta criada

analise_sinasc_janeiro_2019(df_janeiro, 'IDADEMAE', 'DTNASC', 'mean',
                            'Média de Idade da Mãe', 'Data')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/2019-01/' + 'media_idade_mae.png')

analise_sinasc_janeiro_2019(df_janeiro, 'IDADEMAE', 'DTNASC', 'count',
                            'Quantidade de Nascimentos', 'Data')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/2019-01/' + 'qtd_nascimentos.png')

analise_sinasc_janeiro_2019(df_janeiro, 'PESO', 'ESCMAE', 'median',
                            'Peso Mediano', 'Escolaridade da Mãe')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/2019-01/' + 'peso_escolaridade_mae.png')

analise_sinasc_janeiro_2019(df_janeiro, 'APGAR1', 'GESTACAO', 'mean',
                            'APGAR1', 'Tempo de Gestação', 'sort')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/2019-01/' + 'apgar1_tempo_gestacao.png')

analise_sinasc_janeiro_2019(df_janeiro, 'APGAR5', 'GESTACAO', 'mean',
                            'APGAR5', 'Tempo de Gestação', 'sort')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/2019-01/' + 'apgar5_tempo_gestacao.png')

analise_sinasc_janeiro_2019(df_janeiro, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean',
                            'Média Idade Mãe', 'Data', 'unstack')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/2019-01/' + 'qtd_nascimentos_sexo.png')

analise_sinasc_janeiro_2019(df_janeiro, 'PESO', ['DTNASC', 'SEXO'], 'count',
                            'Média Idade Mãe', 'Data', 'unstack')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/2019-01/' + 'peso_sexo.png')