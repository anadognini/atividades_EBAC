import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def analise_mensal(df, value, index, aggfunc, ylabel, xlabel, opcao='nada'):
   if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index, aggfunc=aggfunc).plot(figsize=[15, 5])
   elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index, aggfunc=aggfunc).sort_values(value).plot(figsize=[15, 5])
   elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index, aggfunc=aggfunc).unstack().plot(figsize=[15, 5])

   plt.ylabel(ylabel)
   plt.xlabel(xlabel)

   st.pyplot(fig=plt)
   return None

st.set_page_config(page_title='Análise SINASC RO 2019', page_icon='https://upload.wikimedia.org/wikipedia/commons/f/f1/Bras%C3%A3o_de_Rond%C3%B4nia.svg', layout='wide')

st.write('# Análise dos Dados do SINASC de Rondônia - 2019')

sinasc = pd.read_csv('C:/Users/anado/OneDrive/Documentos/EBAC/M15 - Streamlit I/SINASC_RO_2019.csv')

sinasc.DTNASC = pd.to_datetime(sinasc.DTNASC, format='%Y-%m-%d')

max_date = sinasc.DTNASC.max()
min_date = sinasc.DTNASC.min()

st.sidebar.header('Filtros da Análise')

data_inicial = st.sidebar.date_input('Data inicial', value=min_date, min_value=min_date, max_value=max_date)
data_final = st.sidebar.date_input('Data final', value=max_date, min_value=min_date, max_value=max_date)

sinasc = sinasc[(sinasc['DTNASC'] <= pd.to_datetime(data_final)) & (sinasc['DTNASC'] >= pd.to_datetime(data_inicial))]

analise_mensal(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'Média de Idade da Mãe', 'Data')
analise_mensal(sinasc, 'IDADEMAE', 'DTNASC', 'count', 'Quantidade de Nascimentos', 'Data')
analise_mensal(sinasc, 'PESO', 'ESCMAE', 'median', 'Peso Mediano', 'Escolaridade da Mãe')
analise_mensal(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'APGAR1', 'Tempo de Gestação', 'sort')
analise_mensal(sinasc, 'APGAR5', 'GESTACAO', 'mean', 'APGAR5', 'Tempo de Gestação', 'sort')
analise_mensal(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'Média Idade Mãe', 'Data', 'unstack')
analise_mensal(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'count', 'Média Idade Mãe', 'Data', 'unstack')