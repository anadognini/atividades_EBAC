import streamlit as st
import numpy as np
import pandas as pd
from numpy.random import default_rng as rng
from datetime import datetime
import time

# Acesse os links abaixo, leia o conteúdo e crie uma aplicação com streamlit
# reproduzindo pelo menos 20 códigos extraídos das páginas.

# https://docs.streamlit.io/en/stable/getting_started.html
# https://docs.streamlit.io/en/stable/tutorial/create_a_data_explorer_app.html
# https://docs.streamlit.io/en/stable/advanced_concepts.html
# https://docs.streamlit.io/en/stable/caching.html
# https://docs.streamlit.io/en/stable/api.html
# https://docs.streamlit.io/en/stable/session_state_api.html
# https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py

st.title("Streamlit - Tarefas Práticas")

# 01 - Criando e imprimindo um dataframe com o método st.dataframe()

st.subheader("st.dataframe() - DataFrame Aleatório")

df = pd.DataFrame(
    rng(0).standard_normal((50, 20)), columns=("col %d" % i for i in range(20))
)

st.dataframe(df)

st.markdown('---')

# 02 - Criando e imprimindo uma tabela com o método st.table()

st.subheader("st.table() - Matriz de Confusão")

confusion_matrix = pd.DataFrame(
    {
        "Gato previsto": [85, 3, 2, 1],
        "Cachorro previsto": [2, 78, 4, 0],
        "Pássaro previsto": [1, 5, 72, 3],
        "Peixe previsto": [0, 2, 1, 89],
    },
    index=["Gato real", "Cachorro real", "Pássaro real", "Peixe real"],
)
st.table(confusion_matrix)

st.markdown('---')

# 03 - Slider para selecionar hora de início

st.subheader("st.slider() - Seleção de Hora de Início")

start_time = st.slider(
    "Quando você começou a trabalhar hoje?",
    value=datetime(2026, 1, 1, 9, 30),
    format="DD/MM/YY - hh:mm",
)

st.write("Hora de início:", start_time)

st.markdown('---')

# 04 - Botões com st.button()

st.subheader("st.button() - Botões Simples")

if st.button("Olá", type="primary"): # Botão primário - mais destaque
    st.write("Tchau!")

if st.button("Bonjour", type="secondary"): # Botão secundário - destaque médio
    st.write("Au revoir!")

if st.button("Ciao", type="tertiary"): # Botão terciário - menos destaque
    st.write("Ciao!")

# 05 - Botões em colunas

st.markdown('---')

st.subheader("st.columns() - Botões em Colunas")

left, middle, right = st.columns(3)

if left.button("Botão simples", width="stretch"):
    left.markdown("Você clicou no botão simples.")
if middle.button("Botão emoji", icon="😃", width="stretch"):
    middle.markdown("Você clicou no botão emoji.")
if right.button("Botão material", icon=":material/mood:", width="stretch"):
    right.markdown("Você clicou no botão material.")

st.markdown('---')

# 06 - Selectbox simples

st.subheader("st.selectbox() - Selectbox Simples")

option = st.selectbox(
    "Como você gostaria de ser contatado?",
    ("E-mail", "Telefone residencial", "Telefone móvel"),
)

st.write("Você selecionou:", option)

st.markdown('---')

# 07 - Selectbox com índice e placeholder

st.subheader("st.selectbox() 2 - Índice e Placeholder")

option = st.selectbox(
    "Qual é a cor do céu?",
    ("Rosa", "Verde", "Azul", "Amarelo"),
    index=None, # Nenhum índice selecionado por padrão, inicia vazio
    placeholder="Selecione a cor correta...", # Placeholder personalizado
)

st.write("Você selecionou:", option)

st.markdown('---')

# 08 - Selectbox com opções novas

st.subheader("st.selectbox() 3 - Aceitar Novas Opções")

option = st.selectbox(
    "Qual é o seu animal preferido?",
    ["Gato", "Cachorro", "Pássaro", "Peixe"],
    index=None,
    placeholder="Selecione seu animal preferido...",
    accept_new_options=True, # Permite adicionar novas opções
)

st.write("Você selecionou:", option)

st.markdown('---')

# 09 - Session State

st.subheader("st.session_state - Armazenando Nome do Usuário")

st.text_input("Informe seu nome:", key="name")
st.session_state.name

st.markdown('---')

# 10 - Dataframe e Checkbox

st.subheader("st.checkbox() - Mostrar DataFrame Aleatório")

st.write("Clique na caixa abaixo para mostrar um dataframe aleatório:")

if st.checkbox('Mostrar dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

st.markdown('---')

# 11 - Sidebar com Tìtulo

st.sidebar.title("Eu sou uma sidebar!")

# 12 - Selectbox na sidebar

add_selectbox = st.sidebar.selectbox(
    'Você pode adicionar um selectbox aqui também:',
    ('Opção 1', 'Opção 2', 'Opção 3')
)

st.sidebar.markdown('---')

# 13 - Slider na sidebar

add_slider = st.sidebar.slider(
    'Você pode adicionar um slider aqui também:',
    0.0, 100.0, (25.0, 75.0)
)

# 14 - Radio Buttons

st.subheader("st.radio() - Botões de Rádio")

genre = st.radio(
    "Chapéu-seletor",
    ["Grifinória", "Corvinal", "Lufa-Lufa", "Sonserina"]
)

if genre == "Grifinória":
    st.write("Você está na Grifinória.")
else:
    st.write("Você não está na Grifinória.")

st.markdown('---')

# 15 - Session State para Contador

st.subheader("st.session_state - Contador de Execuções")

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.write(f"Essa página foi executada {st.session_state.counter} vezes.")
st.button("Executar novamente.")  # Botão para reexecutar a página

st.markdown('---')

# 16 - Scatter Chart com Cor Personalizada

st.subheader("st.scatter_chart() - Gráfico de Dispersão com Cor Personalizada")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.write("Escolha a cor dos pontos do gráfico de dispersão abaixo:")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

st.markdown('---')

# 17 - st.metric()

st.subheader("st.metric() - Exibindo Métricas")

left, middle, right = st.columns(3)

left.metric(label="Temperatura", value="25 °C", delta="+1.5 °C")
middle.metric(label="Umidade", value="60 %", delta="-5 %")
right.metric(label="Vento", value="15 km/h", delta="0 km/h")

st.markdown('---')

# 18 - st.balloons()

st.subheader("st.balloons() - Balões de Celebração")

if st.button("Clique para ver balões!"):
    st.balloons()

st.markdown('---')

# 19 - st.cache_data

st.subheader("st.cache_data - Função Cacheada")

@st.cache_data
def expensive_computation(a, b):
    time.sleep(5)  # Simula uma operação demorada
    return a + b

result = expensive_computation(10, 20)

st.write("Resultado da computação cara:", result)

st.markdown('---')

# 20 - Mensagem de Sucesso

st.subheader("st.success() - Mensagem de Sucesso")
st.success("Parabéns! Você concluiu todas as tarefas práticas de Streamlit!")