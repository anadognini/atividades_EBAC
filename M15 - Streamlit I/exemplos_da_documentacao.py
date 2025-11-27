import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Meu primeiro app com Streamlit")

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)  # Exibe o DataFrame interativo

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)
st.dataframe(dataframe.style.highlight_max(axis=0))  # Destaca o valor máximo em cada coluna

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)
st.table(dataframe)  # Exibe o DataFrame como uma tabela estática

x = st.slider('Widget') # Um widget de controle deslizante para selecionar um valor
st.write(x, 'squared is', x * x)

st.write('DataFrame simples:')
st.write(pd.DataFrame({
    'primeira coluna': [1, 2, 3, 4],
    'segunda coluna': [10, 20, 30, 40]
}))

"""
# Meu primeiro app com Streamlit
DataFrame simples:
""" # É possível escrever texto em Markdown diretamente no script

df = pd.DataFrame({
    'primeira coluna': [1, 2, 3, 4],    
    'segunda coluna': [10, 20, 30, 40]
})

df # É possível também printar um dataframe sem precisar do st.write() ou st.dataframe()

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data) # Exibe um gráfico de linhas interativo

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)   

st.map(map_data) # Exibe um mapa interativo com os dados de latitude e longitude

# Simulando um processo com barra de progresso
latest_iteration = st.empty() # Placeholder para atualizar o texto
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteração {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

st.write("Processo concluído!")