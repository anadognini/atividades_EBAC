import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style="whitegrid", rc=custom_params)

@st.cache(show_spinner=True, allow_output_mutation=True)
def load_data(file_data):
    try:
        return pd.read_csv(file_data, sep=';')
    except:
        return pd.read_excel(file_data)

@st.cache(allow_output_mutation=True)
def multiselect_filter(relatorio, col, selecionados):
    if 'all' in selecionados:
        return relatorio
    else:
        return relatorio[relatorio[col].isin(selecionados)].reset_index(drop=True)

@st.cache()
def df_to_string(df):
    return df.to_csv(index=False)

@st.cache_data
def df_to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()
    processed_data = output.getvalue()

    return processed_data

def main():
    st.set_page_config(page_title="Telemarketing Analysis", 
                       page_icon='📞', layout='wide',
                       initial_sidebar_state='expanded')
    st.write('# Telemarketing Analysis 📞')

    ##### Sidebar - Upload de arquivo

    st.sidebar.write("## Subindo arquivos")
    data_file_1 = st.sidebar.file_uploader("Bank Marketing Data",
                                           type=['csv', 'xlsx'])

    if (data_file_1 is not None):
        bank_raw = load_data(data_file_1)
        bank = bank_raw.copy()

        st.write('## Dataset Bruto')
        st.write(bank_raw.head())

        st.write('---')

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

            ################# Tipo de gráfico

            graph_type = st.radio('Selecione o tipo de gráfico', ('Barras', 'Pizza'))

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

        st.write('---')

        ################# Plotando a proporção do target antes e depois dos filtros

        bank_raw_target_perc = bank_raw.y.value_counts(normalize=True).to_frame() * 100
        bank_raw_target_perc = bank_raw_target_perc.sort_index()
        # bank_raw_target_perc

        bank_target_perc = bank.y.value_counts(normalize=True).to_frame() * 100
        bank_target_perc = bank_target_perc.sort_index()
        # bank_target_perc

        ################ Download dos datasets de proporção do target

        col1, col2 = st.columns(2)

        #### Transformando o dataset bruto em excel e fazendo download

        df_xlsx = df_to_excel(bank_raw_target_perc)
        col1.write('### Download do dataset bruto em Excel')
        col1.write(bank_raw_target_perc)
        col1.download_button(label='Download Excel',
                             data=df_xlsx,
                             file_name='bank_raw_target_proportion.xlsx')

        df_xlsx = df_to_excel(bank_target_perc)
        col2.write('### Download do dataset filtrado em Excel')
        col2.write(bank_target_perc)
        col2.download_button(label='Download Excel',
                                data=df_xlsx,
                                file_name='bank_filtered_target_proportion.xlsx')
        
        #### Transformando o dataset bruto em csv e fazendo download

        col3, col4 = st.columns(2)

        df_csv = df_to_string(bank_raw_target_perc)
        col3.write('### Download do dataset bruto em CSV')
        col3.write(bank_raw_target_perc)
        col3.download_button(label='Download CSV',
                             data=df_csv,
                             file_name='bank_raw_target_proportion.csv')

        df_csv = df_to_string(bank_target_perc)
        col4.write('### Download do dataset filtrado em CSV')
        col4.write(bank_target_perc)
        col4.download_button(label='Download CSV',
                                data=df_csv,
                                file_name='bank_filtered_target_proportion.csv')
        st.write('---')

        st.write('## Proporção de Clientes que contrataram o serviço (y)')

        if graph_type == 'Pizza':
            fig, ax = plt.subplots(1, 2, figsize= (12, 6))

            ax[0].pie(bank_raw_target_perc['proportion'], 
                      labels=bank_raw_target_perc.index,
                      autopct='%1.1f%%',
                      startangle=90,
                      textprops={'weight':'bold'})
            ax[0].set_title("Dados brutos", fontweight='bold')

            ax[1].pie(bank_target_perc['proportion'], 
                      labels=bank_target_perc.index,
                      autopct='%1.1f%%',
                      startangle=90,
                      textprops={'weight':'bold'})
            ax[1].set_title("Dados filtrados", fontweight='bold')

            plt.tight_layout()
            st.pyplot(fig)

        else:
            fig, ax = plt.subplots(1, 2, figsize= (12, 6))

            sns.barplot(x=bank_raw_target_perc.index, y="proportion", data=bank_raw_target_perc, ax=ax[0])
            ax[0].bar_label(ax[0].containers[0])
            ax[0].set_title("Dados brutos", fontweight='bold')

            sns.barplot(x=bank_target_perc.index, y="proportion", data=bank_target_perc, ax=ax[1])
            ax[1].bar_label(ax[1].containers[0])
            ax[1].set_title("Dados filtrados", fontweight='bold')

            plt.tight_layout()
            st.pyplot(fig)
    
if __name__ == '__main__':
    main()
