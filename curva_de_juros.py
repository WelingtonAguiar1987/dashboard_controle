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


# Configuração da página
st.set_page_config(page_title='CURVA DE JUROS DOS EUA', page_icon=':money_with_wings:', layout='wide')

# CRIANDO PÁGINA LATERAL ESQUERDA DO SISTEMA:
with st.sidebar:
    st.header('Curva de Juros', divider='rainbow')
    st.image('fed-1200x1200-cropped.JPG')

with st.sidebar:
    st.header('Curva de Juros dos EUA', divider='rainbow')
    data_inicial = st.date_input('Selecione a Data Inicial a Pesquisar: ', format='DD/MM/YYYY')
    data_final = st.date_input('Selecione a Data Final a Pesquisar: ', format='DD/MM/YYYY')

lista_ativos = ['DGS1MO', 'DGS3MO', 'DGS6MO', 'DGS1', 'DGS2', 'DGS5', 'DGS7', 'DGS10', 'DGS20', 'DGS30']

# Certifique-se de que as datas iniciais e finais estão definidas
if data_inicial and data_final:
    # DATAFRAMES PARA A CONSTRUÇÃO DA CURVA DE JUROS
    juros = web.DataReader(lista_ativos, 'fred', data_inicial, data_final)
    

    with st.container():
        st.subheader('Gráfico Interativo da Curva de Juros dos EUA:', divider='rainbow')
        
        # Preparando dados para o gráfico
        fig = go.Figure()
        
        # Adiciona as duas últimas datas ao gráfico
        for data in juros.index[-10000:]:
            fig.add_trace(go.Scatter(x=juros.columns, y=juros.loc[data], mode='lines+markers', name=str(data.date())))
        
        fig.update_layout(title='Curva de Juros',  title_x=0.40, template = 'plotly_dark', title_font_color="#00FFFF", title_font_family="Times New Roman", title_font_size=25,
                          xaxis_title='Prazo/Maturidade',
                          yaxis_title='Taxa de Juros',
                          legend_title='Data')
        fig.update_layout(height=720, width=1080)
        fig.update_xaxes(title_font_family="Times New Roman", title_font_color="#00FF00", title_font_size=18)
        fig.update_yaxes(title_font_family="Times New Roman", title_font_color="#00FF00", title_font_size=18)
        
        # Exibindo o gráfico no Streamlit
        st.plotly_chart(fig, use_container_width=True)
else:
    st.error('Por favor, selecione as datas inicial e final.')
    
st.dataframe(juros)


    
