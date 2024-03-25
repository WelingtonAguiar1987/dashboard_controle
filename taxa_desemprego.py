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


st.set_page_config(page_title='TAXA DE DESEMPREGO EUA', page_icon=':money_with_wings:', layout='wide') 

with st.sidebar:
    st.header('Taxa de Desemprego EUA', divider='rainbow')
    data_inicial = st.date_input('Selecione a Data Inicial a Pesquisar: ', format='DD/MM/YYYY', value=None)
    data_final = st.date_input('Selecione a Data Final a Pesquisar: ', format='DD/MM/YYYY')
    taxa_efetiva_eua = web.DataReader('UNRATE', 'fred', data_inicial, data_final)
    ultima_taxa = taxa_efetiva_eua['UNRATE'][-1]
    
    
with st.container(): 
    st.title('Taxa de Desemprego dos Estados Unidos')
    
with st.spinner('Aguarde por favor...'):
    time.sleep(10)
    
with st.container(): 
    st.subheader('Gráfico da Taxa de Desemprego:', divider='rainbow')
    st.line_chart(taxa_efetiva_eua)
    
with st.container(): 
    st.subheader('Tabela da Taxa de Desemprego:', divider='rainbow')
    st.dataframe(taxa_efetiva_eua)
     
with st.sidebar:
    st.header(f'Taxa Atual de Desemprego: :orange[{ultima_taxa}%]')
    
    

    
    

   






