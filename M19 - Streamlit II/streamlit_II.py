import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style="whitegrid", rc=custom_params)

def multiselect_filter(relatorio, col, selecionados):
    if 'all' in selecionados:
        return relatorio
    else:
        return relatorio[relatorio[col].isin(selecionados)].reset_index(drop=True)

def main():
    st.set_page_config(page_title="Telemarketing Analysis", 
                       page_icon='📞', layout='wide',
                       initial_sidebar_state='expanded')
    st.write('# Telemarketing Analysis 📞')

    bank_raw = pd.read_csv("C:/Users/anado/OneDrive/Documentos/EBAC/M19 - Streamlit II/input/bank-additional-full.csv", sep=';')
    bank = bank_raw.copy()

    st.write('## Dataset Bruto')
    st.write(bank_raw.head())

    st.sidebar.header('Filtros')

    with st.sidebar.form(key='my_form'):

        ################# Filtro de Idade

        max_age = int(bank.age.max())
        min_age = int(bank.age.min())

        idades = st.slider(label='Selecione a faixa etária',
                                min_value=min_age, 
                                max_value=max_age, 
                                value=(min_age, max_age),
                                step=1)
        st.write('---')

        ################ Filtro de profissão

        jobs_list = bank.job.unique().tolist()
        jobs_list.append('all')
        jobs_selected = st.multiselect(label='Selecione as profissões',
                                    options=jobs_list,
                                    default=['all'])
        st.write('---')

        ################# Estado Civil

        marital_list = bank.marital.unique().tolist()
        marital_list.append('all')
        marital_selected = st.multiselect(label='Selecione o estado civil', 
                                          options=marital_list, 
                                          default=['all'])
        st.write('---')

        ################# Default

        default_list = bank.default.unique().tolist()
        default_list.append('all')
        default_selected = st.multiselect(label='Selecione o default', 
                                          options=default_list, 
                                          default=['all'])
        st.write('---')

        ################# Housing

        housing_list = bank.housing.unique().tolist()
        housing_list.append('all')
        housing_selected = st.multiselect(label='Selecione o housing', 
                                          options=housing_list, 
                                          default=['all'])
        st.write('---')

        ################# Loan

        loan_list = bank.loan.unique().tolist()
        loan_list.append('all')
        loan_selected = st.multiselect(label='Selecione o loan', 
                                          options=loan_list, 
                                          default=['all'])

        st.write('---')

        ################# Contact Type

        contact_list = bank.contact.unique().tolist()
        contact_list.append('all')
        contact_selected = st.multiselect(label='Selecione o contato', 
                                          options=contact_list, 
                                          default=['all'])
        st.write('---')

        ################# Month

        month_list = bank.month.unique().tolist()
        month_list.append('all')
        month_selected = st.multiselect(label='Selecione o mês', 
                                          options=month_list, 
                                          default=['all'])
        st.write('---')

        ################# Day of week

        day_list = bank.day_of_week.unique().tolist()
        day_list.append('all')
        day_selected = st.multiselect(label='Selecione o dia da semana', 
                                          options=day_list, 
                                          default=['all'])
        st.write('---')

        ################# Botão de Aplicar Filtros

        bank = (bank.query("age >= @idades[0] & age <= @idades[1]").
                pipe(multiselect_filter, 'job', jobs_selected).
                pipe(multiselect_filter, 'marital', marital_selected).
                pipe(multiselect_filter, 'default', default_selected).
                pipe(multiselect_filter, 'housing', housing_selected).
                pipe(multiselect_filter, 'loan', loan_selected).
                pipe(multiselect_filter, 'contact', contact_selected).
                pipe(multiselect_filter, 'month', month_selected).
                pipe(multiselect_filter, 'day_of_week', day_selected))

        submit_button = st.form_submit_button(label='Aplicar Filtros')

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
