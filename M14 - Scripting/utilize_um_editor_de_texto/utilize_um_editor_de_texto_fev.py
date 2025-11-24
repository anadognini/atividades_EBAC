# Importando as bibliotecas

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Função para criar os gráficos

def analise_sinasc_fevereiro_2019(df, value, index, aggfunc, ylabel, xlabel, opcao='nada'):
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

df_fevereiro = pd.read_csv('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/SINASC_RO_2019_FEV.csv')

# Criando um diretório apenas para o mês de fevereiro

max_data = df_fevereiro.DTNASC.max()[:7]
max_data
os.makedirs('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/' + max_data, exist_ok=True)

# Criando os gráficos e salvando-os na pasta criada

analise_sinasc_fevereiro_2019(df_fevereiro, 'IDADEMAE', 'DTNASC', 'mean',
                            'Média de Idade da Mãe', 'Data')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/2019-02/' + 'media_idade_mae.png')

analise_sinasc_fevereiro_2019(df_fevereiro, 'IDADEMAE', 'DTNASC', 'count',
                            'Quantidade de Nascimentos', 'Data')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/2019-02/' + 'qtd_nascimentos.png')

analise_sinasc_fevereiro_2019(df_fevereiro, 'PESO', 'ESCMAE', 'median',
                            'Peso Mediano', 'Escolaridade da Mãe')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/2019-02/' + 'peso_escolaridade_mae.png')

analise_sinasc_fevereiro_2019(df_fevereiro, 'APGAR1', 'GESTACAO', 'mean',
                            'APGAR1', 'Tempo de Gestação', 'sort')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/2019-02/' + 'apgar1_tempo_gestacao.png')

analise_sinasc_fevereiro_2019(df_fevereiro, 'APGAR5', 'GESTACAO', 'mean',
                            'APGAR5', 'Tempo de Gestação', 'sort')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/2019-02/' + 'apgar5_tempo_gestacao.png')

analise_sinasc_fevereiro_2019(df_fevereiro, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean',
                            'Média Idade Mãe', 'Data', 'unstack')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/2019-02/' + 'qtd_nascimentos_sexo.png')

analise_sinasc_fevereiro_2019(df_fevereiro, 'PESO', ['DTNASC', 'SEXO'], 'count',
                            'Média Idade Mãe', 'Data', 'unstack')
plt.savefig('C:/Users/anado/OneDrive/Documentos/EBAC (2)/M14 - Scripting/output/figs/2019-02/' + 'peso_sexo.png')