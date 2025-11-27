# Importando as bibliotecas

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

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

meses = sys.argv[1:] # # lista: ['JAN', 'FEV', 'MAR', 'ABR', ...]

if not meses:
    print("Uso: python script.py JAN FEV MAR ...")
    sys.exit(1)

for mes in meses:
    print(f"Processando mês: {mes}")

    # Lendo o dataframe do mês
    caminho_csv = (
        'C:/Users/anado/OneDrive/Documentos/EBAC/M14 - Scripting/'
        f'SINASC_RO_2019_{mes}.csv'
    )
    sinasc = pd.read_csv(caminho_csv)

    # Criando um diretório apenas para o mês em questão
    max_data = sinasc.DTNASC.max()[:7]
    print("Max data:", max_data)

    pasta_saida = (
        'C:/Users/anado/OneDrive/Documentos/EBAC/M14 - Scripting/output/figs/'
        + max_data
    )
    os.makedirs(pasta_saida, exist_ok=True)

    # Criando os gráficos e salvando-os na pasta criada

    analise_mensal(sinasc, 'IDADEMAE', 'DTNASC', 'mean',
                   'Média de Idade da Mãe', 'Data')
    plt.savefig(pasta_saida + '/media_idade_mae.png')
    plt.close()  # limpa a figura atual

    analise_mensal(sinasc, 'IDADEMAE', 'DTNASC', 'count',
                   'Quantidade de Nascimentos', 'Data')
    plt.savefig(pasta_saida + '/qtd_nascimentos.png')
    plt.close()

    analise_mensal(sinasc, 'PESO', 'ESCMAE', 'median',
                   'Peso Mediano', 'Escolaridade da Mãe')
    plt.savefig(pasta_saida + '/peso_escolaridade_mae.png')
    plt.close()

    analise_mensal(sinasc, 'APGAR1', 'GESTACAO', 'mean',
                   'APGAR1', 'Tempo de Gestação', 'sort')
    plt.savefig(pasta_saida + '/apgar1_tempo_gestacao.png')
    plt.close()

    analise_mensal(sinasc, 'APGAR5', 'GESTACAO', 'mean',
                   'APGAR5', 'Tempo de Gestação', 'sort')
    plt.savefig(pasta_saida + '/apgar5_tempo_gestacao.png')
    plt.close()

    analise_mensal(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean',
                   'Média Idade Mãe', 'Data', 'unstack')
    plt.savefig(pasta_saida + '/qtd_nascimentos_sexo.png')
    plt.close()

    analise_mensal(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'count',
                   'Média Idade Mãe', 'Data', 'unstack')
    plt.savefig(pasta_saida + '/peso_sexo.png')
    plt.close()

    print(f"Concluído mês: {mes}\n")