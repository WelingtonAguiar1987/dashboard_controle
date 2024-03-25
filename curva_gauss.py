import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from scipy.stats import norm
import plotly.graph_objs as go



st.set_page_config(page_title='CURVA DE GAUSS', page_icon=':chart_with_upwards_trend:', layout='wide')

# Define o título da aplicação web
st.title('Análise Interativa da Curva de Gauss do Nasdaq Futuros')

# Inputs para seleção das datas
with st.sidebar:
    st.header('Curva de Gauss', divider='rainbow')
    st.image('gauss.JPEG')
    start_date = st.date_input('Selecione a data inicial:', value=pd.to_datetime('2023-03-17'), format='DD/MM/YYYY')
    end_date = st.date_input('Selecione a data final:', value=pd.to_datetime('2024-06-21'), format='DD/MM/YYYY')
    



# Função para carregar os dados do Yahoo Finance
def load_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Carrega os dados do MNQ=F
data = load_data('MNQ=F')

# Verifica se há dados para processar
if not data.empty:
    # Calcula a média e o desvio padrão dos preços de fechamento ajustados
    mu = data['Adj Close'].mean()
    sigma = data['Adj Close'].std()
    last_price = data['Adj Close'][-1]
    
    # Calcula a mediana dos preços de fechamento ajustados
    median = data['Adj Close'].median()
    
    # Cria um intervalo de preços com base na média e desvio padrão
    prices = np.linspace(data['Adj Close'].min(), data['Adj Close'].max(), 100)
    
    # Ajusta a curva de Gauss aos preços do ativo
    density = norm.pdf(prices, mu, sigma)
    
    # Cria o gráfico interativo com Plotly
    fig = go.Figure()

    # Adiciona a curva de Gauss
    fig.add_trace(go.Scatter(x=density, y=prices, mode='lines', name='Curva de Gauss', line_color="#00FFFF"))

    # Adiciona linhas para a média, desvios padrões e último preço
    fig.add_hline(y=mu, line=dict(color='red', width=2, dash='dash'), name='Média')
    fig.add_hline(y=mu + sigma, line=dict(color='green', width=2, dash='dot'), name='+1 Desvio Padrão')
    fig.add_hline(y=mu - sigma, line=dict(color='blue', width=2, dash='dot'), name='-1 Desvio Padrão')
    fig.add_hline(y=mu + 2*sigma, line=dict(color='green', width=2, dash='dashdot'), name='+2 Desvios Padrões')
    fig.add_hline(y=mu - 2*sigma, line=dict(color='blue', width=2, dash='dashdot'), name='-2 Desvios Padrões')
    fig.add_hline(y=last_price, line=dict(color='purple', width=2, dash='dot'), name='Último Preço')
    
    # Adiciona a linha da mediana ao gráfico
    fig.add_hline(y=median, line=dict(color='orange', width=2, dash='dash'), name='Mediana')

    # Adiciona anotações para média, desvios padrões, último preço e mediana
    fig.add_annotation(xref="paper", x=0.05, y=mu,
                       text=f"Média: {mu:.2f}", showarrow=False, bgcolor="red")
    fig.add_annotation(xref="paper", x=0.05, y=mu + sigma,
                       text=f"+1 Desvio Padrão: {mu + sigma:.2f}", showarrow=False, bgcolor="green")
    fig.add_annotation(xref="paper", x=0.05, y=mu - sigma,
                       text=f"-1 Desvio Padrão: {mu - sigma:.2f}", showarrow=False, bgcolor="blue")
    fig.add_annotation(xref="paper", x=0.05, y=mu + 2*sigma,
                       text=f"+2 Desvios Padrões: {mu + 2*sigma:.2f}", showarrow=False, bgcolor="green")
    fig.add_annotation(xref="paper", x=0.05, y=mu - 2*sigma,
                       text=f"-2 Desvios Padrões: {mu - 2*sigma:.2f}", showarrow=False, bgcolor="blue")
    fig.add_annotation(xref="paper", x=0.95, y=last_price,
                       text=f"Último Preço: {last_price:.2f}", showarrow=False, bgcolor="purple", font=dict(color="white"))
    fig.add_annotation(xref="paper", x=0.95, y=median,
                       text=f"Mediana: {median:.2f}", showarrow=False, bgcolor="orange", font=dict(color="white"))

    # Configurações adicionais do layout
    fig.update_layout(title='Curva de Gauss dos Preços de Fechamento Ajustados', template='plotly_dark',
                      title_x=0.35, title_font_color="#00FFFF", title_font_family="Times New Roman", title_font_size=22,
                      xaxis_title='Densidade de Probabilidade', 
                      yaxis_title='Preço de Fechamento Ajustado',
                      margin=dict(l=0, r=0, t=30, b=0), height=720, width=1080)
    fig.update_xaxes(title_font_family="Times New Roman", title_font_color="#00FF00", title_font_size=18)
    fig.update_yaxes(title_font_family="Times New Roman", title_font_color="#00FF00", title_font_size=18)

    # Mostra o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write("Nenhum dado disponível para o período selecionado. Por favor, selecione outro intervalo de datas.")
    
with st.sidebar:
    st.write(f'Distância entre Desvios Padrões: :blue[{sigma:.2f}]')
    st.write(f'Média: :red[{mu:.2f}]')
    st.write(f'Mediana: :orange[{median:.2f}]')
    

