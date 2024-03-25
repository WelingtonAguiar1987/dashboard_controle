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
import pandas_datareader.data as web


st.set_page_config(page_title='TAXA DO CPI - EUA', page_icon=':money_with_wings:', layout='wide') 

with st.sidebar:
    st.header('Índice de Preços no Consumidor menos Alimentos e Energia - EUA', divider='rainbow')
    data_inicial = st.date_input('Selecione a Data Inicial a Pesquisar: ', format='DD/MM/YYYY', value=None)
    data_final = st.date_input('Selecione a Data Final a Pesquisar: ', format='DD/MM/YYYY')
    
    # Índice de Preços no Consumidor: Todos os Itens: Total para Estados Unidos:
    inflacao_eua = web.DataReader('USACPALTT01CTGYM', 'fred', data_inicial, data_final)
    inflacao_ultima_taxa = inflacao_eua['USACPALTT01CTGYM'][-1]
    
    # Índice de Preços no Consumidor menos Alimentos e Energia:
    cpi_eua = web.DataReader('CORESTICKM159SFRBATL', 'fred', data_inicial, data_final)
    cpi_ultima_taxa = cpi_eua['CORESTICKM159SFRBATL'][-1]
    
    # Índice de Preços ao Consumidor para Todos os Consumidores Urbanos: Todos os Itens na Média das Cidades dos EUA:
    cpi_todos_eua = web.DataReader('CPIAUCSL', 'fred', data_inicial, data_final)
    cpi_todos_ultima_taxa = cpi_todos_eua['CPIAUCSL'][-1]
    cpi_todos_eua['Retorno Acumulado'] = cpi_todos_eua['CPIAUCSL'].pct_change() * 100
    
with st.container(): 
    st.title('Índice de Preços no Consumidor menos Alimentos e Energia dos Estados Unidos')
    
with st.spinner('Aguarde por favor...'):
    time.sleep(10)
 
# Gráficos dos dados de inflação:     
with st.container(): 
    st.subheader('Gráfico de Índice de Preços no Consumidor: Todos os Itens: Total para Estados Unidos:', divider='rainbow')
    st.line_chart(inflacao_eua)
    
with st.container(): 
    st.subheader('Gráfico de Índice de Preços no Consumidor menos Alimentos e Energia dos EUA:', divider='rainbow')
    st.line_chart(cpi_eua)
    
with st.container(): 
    st.subheader('Gráfico de Índice de Preços ao Consumidor para Todos os Consumidores Urbanos: Todos os Itens na Média das Cidades dos EUA:', divider='rainbow')
    st.line_chart(cpi_todos_eua)

# Tabelas dos dados de inflação:  
with st.container(): 
    st.subheader('Tabela de Índice de Preços no Consumidor: Todos os Itens: Total para Estados Unidos:', divider='rainbow')
    st.dataframe(inflacao_eua)
 
with st.container(): 
    st.subheader('Tabela de Índice de Preços no Consumidor menos Alimentos e Energia dos EUA:', divider='rainbow')
    st.dataframe(cpi_eua)
    
with st.container(): 
    st.subheader('Tabela de Índice de Preços ao Consumidor para Todos os Consumidores Urbanos: Todos os Itens na Média das Cidades dos EUA:', divider='rainbow')
    st.dataframe(cpi_todos_eua)
    
with st.sidebar:
    st.header(f'Taxa Anual CPI Atual Todos Itens: :orange[{inflacao_ultima_taxa:.2f}%]')
     
with st.sidebar:
    st.header(f'Taxa Anual Atual do CPI: :orange[{cpi_ultima_taxa:.2f}%]')
     
with st.sidebar:
    st.header(f'Cesta CPI Atual - Média Cidades: :orange[{cpi_todos_ultima_taxa:.2f}]')
    
    

    
    

   






