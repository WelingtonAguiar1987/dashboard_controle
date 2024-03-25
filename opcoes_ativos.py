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

# CONFIGURAÇÃO DE PÁGINA:
st.set_page_config(page_title='OPÇÕES DE ATIVOS PARA ANALISAR', page_icon=':control_knobs:', layout='wide')

# CRIANDO ABA LATERAL ESQUERDA DE CONTROLE DO SISTEMA:
with st.sidebar:
    st.header('Opções de Ativos para Analisar', divider='rainbow')
    st.image('CME-Group-contratos.JPG')
    st.divider()
    
# DETALHES DO ATIVO:
futuros = {
    'MICRO NASDAQ': {'sigla': 'MNQ=F', 'tick': 0.25, 'valor tick': 0.50},
    'MINI NASDAQ': {'sigla': 'NQ=F', 'tick': 0.25, 'valor tick': 5.00},
    
    'MICRO S&P500': {'sigla': 'MES=F', 'tick': 0.25, 'valor tick': 1.25},
    'MINI S&P500': {'sigla': 'ES=F', 'tick': 0.25, 'valor tick': 12.50},
    
    'MICRO DOW JONES': {'sigla': 'MYM=F', 'tick': 1.00, 'valor tick': 0.50},
    'MINI DOW JONES': {'sigla': 'YM=F', 'tick': 1.00, 'valor tick': 5.00},
    
    'MICRO RUSSELL 2000': {'sigla': 'M2K=F', 'tick': 0.10, 'valor tick': 0.50},   
    'MINI RUSSELL 2000': {'sigla': 'RTY=F', 'tick': 0.10, 'valor tick': 5.00}  
}

# ACRESCENTANDO ÍTENS NA ABA ESQUERDA:
with st.sidebar:
    selecao_ativos = st.selectbox('Selecione o ativo a analisar: ', futuros)
    
with st.container():
    st.title('Opções de Ativos para Analisar')
       
if selecao_ativos == 'MICRO NASDAQ':
    for i in futuros:
        x = i
        st.write(x)
    
    





