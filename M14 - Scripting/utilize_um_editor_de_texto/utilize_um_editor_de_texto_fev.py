# Importando as bibliotecas

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Função para criar os gráficos

def analise_mensal(df, value, index, aggfunc, ylabel, xlabel, opcao='nada'):
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

sinasc = pd.read_csv('C:/Users/anado/OneDrive/Documentos/EBAC (2)/Dados/SINASC_RO_2019_FEV.csv')

# Criando um diretório apenas para o mês em questão

max_data = sinasc.DTNASC.max()[:7]
max_data

os.makedirs('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/' + max_data, exist_ok=True)

# Criando os gráficos e salvando-os na pasta criada

analise_mensal(sinasc, 'IDADEMAE', 'DTNASC', 'mean',
                            'Média de Idade da Mãe', 'Data')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/' + max_data + '/media_idade_mae.png')

analise_mensal(sinasc, 'IDADEMAE', 'DTNASC', 'count',
                            'Quantidade de Nascimentos', 'Data')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/' + max_data + '/qtd_nascimentos.png')

analise_mensal(sinasc, 'PESO', 'ESCMAE', 'median',
                            'Peso Mediano', 'Escolaridade da Mãe')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/' + max_data + '/peso_escolaridade_mae.png')

analise_mensal(sinasc, 'APGAR1', 'GESTACAO', 'mean',
                            'APGAR1', 'Tempo de Gestação', 'sort')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/' + max_data + '/apgar1_tempo_gestacao.png')

analise_mensal(sinasc, 'APGAR5', 'GESTACAO', 'mean',
                            'APGAR5', 'Tempo de Gestação', 'sort')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/' + max_data + '/apgar5_tempo_gestacao.png')

analise_mensal(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean',
                            'Média Idade Mãe', 'Data', 'unstack')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/' + max_data + '/qtd_nascimentos_sexo.png')

analise_mensal(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'count',
                            'Média Idade Mãe', 'Data', 'unstack')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/' + max_data + '/peso_sexo.png')
