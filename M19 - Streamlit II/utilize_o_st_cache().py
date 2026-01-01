import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import timeit

@st.cache
def load_data(file_data):
    return pd.read_csv(file_data, sep=';')

def main():
    st.write('# Telemarketing Analysis 📞')
    st.markdown('---')
    
    start = timeit.default_timer()
    bank_raw = load_data("C:/Users/anado/OneDrive/Documentos/EBAC/M19 - Streamlit II/input/bank_maior.csv")

    st.write('Time: ', timeit.default_timer() - start)
    st.write(bank_raw.head())

if __name__ == '__main__':
    main()