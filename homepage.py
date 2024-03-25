import streamlit as st


st.set_page_config(page_title='HOMEPAGE', page_icon=':left_luggage:', layout='wide')

with st.container():
    
    with st.sidebar:
        st.page_link('homepage.py', label="Homepage", icon="🏠")
        st.image('sm_5afa953403584.JPG')
        st.divider()
    
    st.title('Análise de Volatilidade do Nasdaq Futuros')
    st.image('CME_Group_and_Nasdaq_Logo.JPG')
    st.text('Introdução: Esse dashboard serve para fazer cálculos estatísticos para nos orientar qual \n a volatilidade média do ativo em questão. Através dele, podemos ter uma "estimativa" de \nonde "provavelmente", o ativo poderá realizar correções, alvos ou até mesmo stops. \n Através dessa ferramenta, também podemos monitorar como está a Taxa Efetiva de Juros, \n Curva de Juros, volatilidades analisadas com base na Curva de Gauss e futuramente o \n VAR (Value At Risk). Com esta ferramente também podemos calcular o peso das operações \n com base em quantidades de contratos operados e saldo em conta, assim como o payoff em \n questão.')
    st.subheader('Criador: Welington Monteiro Aguiar')