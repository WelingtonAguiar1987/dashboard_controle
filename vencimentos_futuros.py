# BIBLIOTECAS IMPORTADAS:
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import datetime
from datetime import timedelta
import streamlit as st
import time

# VENCIMENTOS DO ATIVO NO ANO:
primeiro_vencimento = 'MNQM24.CME',
segundo_vencimento = 'MNQU24.CME',
terceiro_vencimento =  'MNQZ24.CME',
quarto_vencimento =  'MNQH25.CME'

# CONFIGURAÇÃO DO SISTEMA:
st.set_page_config(page_title='VENCIMENTOS FUTUROS', page_icon=':dollar:', layout='wide')

# CRIANDO ABA ESQUERDA DE CONTROLE DO SISTEMA:
with st.sidebar:
    st.header('Vencimentos Futuros de 2024', divider='rainbow')
    st.image('imagem_wallstreet.JPG')
    data_inicial = st.date_input('Selecione a data Inicial de Pesquisa: ', format='DD/MM/YYYY')
    
    periodo = ['5m', '15m', '30m', '60m']
    
    selecao_periodo = st.selectbox('Selecione o Período dos Gráficos: ', periodo)
    
# DATAFRAME DOS ATIVOS DE VENCIMENTO:
df_vencimento_1 = yf.download(primeiro_vencimento, start=data_inicial, end= datetime.date.today(), interval=selecao_periodo)
df_vencimento_2 = yf.download(segundo_vencimento, start=data_inicial, end= datetime.date.today(), interval=selecao_periodo)
df_vencimento_3 = yf.download(terceiro_vencimento, start=data_inicial, end= datetime.date.today(), interval=selecao_periodo)
df_vencimento_4 = yf.download(quarto_vencimento, start=data_inicial, end= datetime.date.today(), interval=selecao_periodo)

# TÍTULO DA PÁGINA PRINCIPAL:
st.title('Futuros de Nasdaq')   

# CRIANDO COLUNAS:  
coluna_1, coluna_2 = st.columns(2, gap='large')

with st.container(): 
    with coluna_1:
        st.subheader('MNQM4:', divider='rainbow')
        df_grafico_1 = st.line_chart(df_vencimento_1['Adj Close'])
    
    with coluna_2:
        st.subheader('MNQU4:', divider='rainbow')
        df_grafico_2 = st.line_chart(df_vencimento_2['Adj Close'])
    
    coluna_3, coluna_4 = st.columns(2, gap='large')
    with coluna_3:
        st.subheader('MNQZ4:', divider='rainbow')
        df_grafico_3 = st.line_chart(df_vencimento_3['Adj Close'])
    
    with coluna_4:
        st.subheader('MNQH5:', divider='rainbow')
        df_grafico_4 = st.line_chart(df_vencimento_4['Adj Close'])
    
    
    
    
    


    
    


    
    