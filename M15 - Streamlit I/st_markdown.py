import streamlit as st

st.title('Título da Aplicação Web')

st.header('Cabeçalho da Seção')

st.subheader('Subcabeçalho da Seção')

st.markdown('Este é um exemplo de **aplicação web** usando Streamlit. Você pode adicionar *texto em itálico*, listas, links e muito mais!')
st.markdown("# Isso aqui é um título! [#]")
st.markdown("## Isso aqui é um subtítulo! [##]")
st.markdown("### Isso aqui é um sub-subtítulo! [###]")
st.markdown("#### Isso aqui é um sub-sub-subtítulo! [####]")
st.markdown("##### Isso aqui é um sub-sub-sub-subtítulo! [#####]")
st.markdown("###### Isso aqui é um sub-sub-sub-sub-subtítulo! [######]")
st.markdown("""
Aqui está uma lista não ordenada:
- Item 1
- Item 2
- Item 3
""")
st.markdown("""Aqui está uma lista ordenada:
1. Primeiro item
2. Segundo item
3. Terceiro item
""")
st.markdown("Para mais informações, visite o [site oficial do Streamlit](https://streamlit.io).")
st.markdown('> Este é um bloco de citação em Markdown.')
st.markdown('---')  # Linha horizontal para separação
st.markdown('Você também pode adicionar código em linha, como `print("Olá, Mundo!")`, ou blocos de código:')
st.markdown('```python\ndef saudacao():\n    return "Olá, Mundo!"\n```') 
st.markdown('<h1 style="color:blue;">Título em HTML</h1>', unsafe_allow_html=True) 
st.markdown('''
| MARKDOWN  | PEQUENO | GRANDE      |
|-----------|---------|-------------|
| *itálico* | 'code'  | **negrito** |
 ''')

st.code('''
def saudacao():         
    return "Olá, Mundo!"
''', language='python')

st.image('https://preview.redd.it/meu-gato-%C3%A9-praticamente-o-gato-do-meme-v0-n9dleoj8dgfc1.jpg?width=640&crop=smart&auto=webp&s=52de2578fe227e639db822d551bba33c6d28a2f1', caption='A imagem mais linda do mundo')

st.video('https://www.youtube.com/watch?v=JwSS70SZdyM')

st.dataframe({
    'Coluna 1': [1, 2, 3],  
    'Coluna 2': ['A', 'B', 'C']
})

