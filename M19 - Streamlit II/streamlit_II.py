import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.set_page_config(page_title="Telemarketing Analysis", 
                       page_icon='📞', layout='wide',
                       initial_sidebar_state='expanded')
    st.write('# Telemarketing Analysis 📞')

    bank_raw = pd.read_csv("C:/Users/anado/OneDrive/Documentos/EBAC/M19 - Streamlit II/input/bank-additional-full.csv", sep=';')
    bank = bank_raw.copy()

    st.sidebar.header('Filtros')

    st.write('## Dataset Bruto')
    st.write(bank_raw.head())

    ################# Filtro de Idade

    max_age = int(bank.age.max())
    min_age = int(bank.age.min())

    idades = st.sidebar.slider(label='Selecione a faixa etária',
                               min_value=min_age, 
                               max_value=max_age, 
                               value=(min_age, max_age),
                               step=1)
    
    st.sidebar.write('Idades selecionadas:', idades)
    st.sidebar.write('Idade min:', idades[0],' | Idade max:', idades[1])

    bank = bank[(bank['age'] >= idades[0]) & (bank['age'] <= idades[1])]

    st.sidebar.write('---')

    ################ Filtro de profissão

    jobs_list = bank.job.unique().tolist()
    
    jobs_selected = st.sidebar.multiselect(label='Selecione as profissões',
                                  options=jobs_list,
                                  default=jobs_list)
    
    st.sidebar.write('Profissões selecionadas:', jobs_selected)
    
    bank = bank[bank['job'].isin(jobs_selected)].reset_index(drop=True)

    ################ Dataset após filtros

    st.write('## Dataset Após Filtros')
    st.write(bank.head())

    bank_raw_target_perc = bank_raw.y.value_counts(normalize=True).to_frame() * 100
    bank_raw_target_perc = bank_raw_target_perc.sort_index()
    # bank_raw_target_perc

    bank_target_perc = bank.y.value_counts(normalize=True).to_frame() * 100
    bank_target_perc = bank_target_perc.sort_index()
    # bank_target_perc

    st.write('## Proporção de Clientes que contrataram o serviço (y)')

    fig, ax = plt.subplots(1, 2, figsize= (12, 6))

    sns.barplot(x=bank_raw_target_perc.index, y="proportion", data=bank_raw_target_perc, ax=ax[0])
    ax[0].bar_label(ax[0].containers[0])
    ax[0].set_title("Dados brutos", fontweight='bold')

    sns.barplot(x=bank_target_perc.index, y="proportion", data=bank_target_perc, ax=ax[1])
    ax[1].bar_label(ax[1].containers[0])
    ax[1].set_title("Dados filtrados", fontweight='bold')

    plt.tight_layout()
    st.pyplot(fig)
    
main()
