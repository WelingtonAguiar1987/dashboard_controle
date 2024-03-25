# BIBLIOTECAS IMPORTADAS:
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
import datetime
from datetime import timedelta
import streamlit as st
import time
from datetime import date


# FUNÇÃO CRIAR LINHAS:
def linha():
    print('-' * 37)


# SIGLA E NOME DO ATIVO ANALISADO:
sigla_ativo = "MNQ=F"
nome_ativo = "NASDAQ 100 FUTUROS"

data_hoje = datetime.date.today()
data_hoje.isoformat()


# DEMARCAÇÃO NO GRÁFICO DO DIA ATUAL:
adicao_data_marcacao = timedelta(1)
inicio_negociacao_atual = data_hoje - adicao_data_marcacao
inicio_marcacao = data_hoje
final_marcacao = data_hoje + adicao_data_marcacao


# DADOS HISTÓRICOS PERÍODO DE VENCIMENTO:
data_inicial_vencimento = '2023-03-17'
data_final_vencimento = '2024-06-21'

dados_historico_vencimento = yf.download(sigla_ativo, data_inicial_vencimento, data_final_vencimento, interval='1d')  # Dataframe do atual vencimento do ativo:
dados_historico_vencimento['Volatilidade'] = dados_historico_vencimento['High'] - dados_historico_vencimento['Low']  # Adicionando uma coluna de Volatilidade em pontos:
volatilidade_do_dia = dados_historico_vencimento['Volatilidade'][-1]  # Volatilidade do dia atual:
volume_dia = dados_historico_vencimento['Volume'][-1] # Volume


# DADOS DE ESTATÍSTICA:
media = np.mean(dados_historico_vencimento['Close'])
mediana = np.median(dados_historico_vencimento['Close'])

# FILTRO DE TODO O PERÍODO DE VENCIMENTO:
periodo_vencimento_filtrado = dados_historico_vencimento['Volatilidade'][0:-1]


# QUANTIDADE DE PREGÃO NO PERÍODO:
quantidade_pregao = dados_historico_vencimento['Close'].count()


# CÁLCULO DO DESVIO PADRÃO DE TODO ESSE VENCIMENTO:
desvio_padrao = np.std(periodo_vencimento_filtrado)
meio_desvio_padrao = desvio_padrao / 2


st.set_page_config(page_title='DAYTRADING', page_icon='	:chart_with_upwards_trend:', layout='wide')

with st.sidebar:
    st.header('Daytrading', divider='rainbow')
    st.image('360_F_650871585_ewsogG34QATtQylTcmC6afo5Bni1anlv.JPG')

    
    periodo = ['5m', '15m', '30m', '60m']
    
    selecao_periodo = st.selectbox('Selecione o Período do Gráfico: ', periodo)

    lista_desvios_padroes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    selecao_desvios_padroes = st.selectbox('Selecione a quantidade de Meios Desvios Padrões: ', lista_desvios_padroes)
    
    lista_entradas = ['Automático', 'Manual']
    selecao_entradas = st.selectbox('Selecione o tipo de dados da Última Abertura e Último Fechamento', lista_entradas)
    

    


# DADOS HISTÓRICOS PERÍODO INTRADAY:
adicao_data_intraday = timedelta(1)
subtracao_data_intraday = timedelta(1)
data_inicial_intraday = data_hoje - adicao_data_intraday
data_final_intraday = data_hoje + subtracao_data_intraday

dados_historico_intraday = yf.download(sigla_ativo, data_inicial_intraday, data_final_intraday, interval=selecao_periodo)

maxima = dados_historico_intraday['High']
maxima_dia = dados_historico_vencimento['High'][-1]

minima = dados_historico_intraday['Low']
minima_dia = dados_historico_vencimento['Low'][-1]


ultimo_preco = dados_historico_intraday['Close'][-1]

ultima_maxima = dados_historico_intraday['High'][-1]
ultima_minima = dados_historico_intraday['Low'][-1]


# DATA DO PREGÃO ATUAL:
pregao_atual = dados_historico_vencimento.index[-1]


# PREÇO DO ÚLTIMO FECHAMENTO E ÚLTIMA ABERTURA:
# PREENCHER OS VALORES ABAIXO:

with st.sidebar:
    if selecao_entradas == 'Automático':
        preco_ultimo_fechamento = dados_historico_vencimento['Close'][-2]
        ultima_abertura = dados_historico_vencimento['Open'][-1]
    
    else:
        preco_ultimo_fechamento = st.number_input('Digite o Preço do Último Fechamento: ')
        ultima_abertura = st.number_input('Digite o Preço da Última Abertura: ')

# VARIAÇÃO DO DIA:
variacao_dia_pontos = (ultimo_preco - preco_ultimo_fechamento)
variacao_fator = (variacao_dia_pontos / preco_ultimo_fechamento)
variacao_percentual = variacao_fator * 100

if ultimo_preco >= preco_ultimo_fechamento:
    variacao_dia_pontos = (ultimo_preco - preco_ultimo_fechamento)
else:
    variacao_dia_pontos = (ultimo_preco - preco_ultimo_fechamento)
    


# CÁLCULO PARA ANÁLISE DESVIO PADRÃO:*
mais_2dp = (preco_ultimo_fechamento + (desvio_padrao * 2))                                                                                         
mais_1dp_e_meio = (preco_ultimo_fechamento + (meio_desvio_padrao * 3))
mais_1dp = (preco_ultimo_fechamento + (desvio_padrao))
mais_meio_desvio_padrao = (preco_ultimo_fechamento + meio_desvio_padrao)

menos_meio_desvio_padrao = (preco_ultimo_fechamento - meio_desvio_padrao)
menos_1dp = (preco_ultimo_fechamento - (desvio_padrao))
menos_1dp_e_meio = (preco_ultimo_fechamento - (meio_desvio_padrao * 3))
menos_2dp = (preco_ultimo_fechamento - (desvio_padrao * 2))


def gerar_dp(meio_desvio_padrao):
    input_dp = int(selecao_desvios_padroes)
    lista_dps = []

    # Gerando desvios padrões positivos e negativos
    for i in range(-input_dp, input_dp + 1):
        if i != 0:  # Ignorando o zero
            total_meio_dp = i * meio_desvio_padrao
            lista_dps.append((i * 0.5, total_meio_dp))

    return lista_dps

# Substitua '10' pelo valor real do seu meio desvio padrão
meio_desvio_padrao = meio_desvio_padrao
df_dp = pd.DataFrame(gerar_dp(meio_desvio_padrao), columns=['DESVIOS PADRÕES', 'VALOR POR DP'])
df_dp['NÍVEIS DE PREÇO'] = preco_ultimo_fechamento + df_dp['VALOR POR DP']

# Adicionando um índice ao DataFrame
df_dp.index = pd.RangeIndex(start=1, stop=len(df_dp) + 1, step=1)

# CÁLCULO DE GAP DE ABERTURA COM BASE NO GRÁFICO DIÁRIO:
if ultima_abertura > preco_ultimo_fechamento:
    gap_diario = ultima_abertura - preco_ultimo_fechamento
    posicao_gap_diario = str(f':green[GAP DE ALTA]')
    
else:
    gap_diario = preco_ultimo_fechamento - ultima_abertura
    posicao_gap_diario = str(f':red[GAP DE BAIXA]')
    
    
# CÁLCULO DE GAP DE ABERTURA COM BASE NO GRÁFICO INTRADAY:
if ultima_abertura > preco_ultimo_fechamento: # ESTÁ EM DESUSO:
    gap_intraday = ultima_abertura - preco_ultimo_fechamento
    posicao_gap_intraday = str(f':green[GAP DE ALTA]')
    
else:
    gap_intraday = preco_ultimo_fechamento - ultima_abertura
    posicao_gap_intraday = str(f':red[GAP DE BAIXA]')
    
# VARIAÇÃO PERCENTUAL DA ABERTURA EM GAP:


variacao_gap_pontos = (ultima_abertura - preco_ultimo_fechamento)
variacao_gap_fator = (variacao_gap_pontos / preco_ultimo_fechamento)
variacao_gap_percentual = variacao_gap_fator * 100


if ultima_abertura < preco_ultimo_fechamento:
    percentual_gap = (ultima_abertura / preco_ultimo_fechamento)
    
else:
    percentual_gap = (ultima_abertura / preco_ultimo_fechamento)
    
    
# LAÇO FOR INTRADAY:


# CRIANDO SIDEBAR COM DADOS GERAIS DO ATIVO:
with st.sidebar:
    st.divider()
    st.header('Relatório do Ativo:')
    
    st.write(f'Média: :orange[{media:.2f}.]')
    st.write(f'Mediana: :orange[{mediana:.2f}.]')
 
    
    st.write(f'Desvio Padrão: :orange[{desvio_padrao:.2f} Pontos.]')
    st.write(f'Meio Desvio Padrão: :orange[{meio_desvio_padrao:.2f} Pontos.]')
    st.write(f'Volatilidade de Hoje: :orange[{volatilidade_do_dia:.2f}.]')
    st.write(f'Total de pregões analisados: :orange[{quantidade_pregao}.]')
    st.write(f'Data inicial do contrato: :orange[{data_inicial_vencimento}.]')
    st.write(f'Data final do contrato: :orange[{data_final_vencimento}.]')
    st.write(f'Cálculo para Daytrade no dia:\n :orange[{data_hoje}.]')
    st.write(f'Gráfico visualizado entre os dias:    \n:orange[{data_inicial_intraday} ao {data_final_intraday}.]')
    st.divider()
    
    st.header('Dados de Mercado:')
    st.markdown(f'Último Preço: :violet[{ultimo_preco:.2f}]')
    st.write(f'Última Abertura: {ultima_abertura:.2f}')
    st.markdown(f'Máxima: :green[{maxima_dia:.2f}]')
    st.markdown(f'Mínima: :red[{minima_dia:.2f}]')
    st.markdown(f'Último Fechamento: :blue[{preco_ultimo_fechamento:.2f}]')
    st.markdown(f'Volume do dia: {volume_dia}')
    st.divider()
    st.header('Gap de Abertura (diário):')
    st.markdown(f'Sentido do GAP: {posicao_gap_diario}')
    
# CONDICIONAL PARA DEFINIR PONTUAÇÃO E PERCENTUAIS DE VARIAÇÃO DO DIA:   
with st.sidebar:   
    if variacao_gap_percentual >= 0:
        st.metric(label="Variação GAP Abertura: ", value=f"{variacao_gap_pontos:.2f} Pontos.", delta=f"{variacao_gap_percentual:.2f}%")
    else:
        st.metric(label="Variação GAP Abertura: ", value=f"{variacao_gap_pontos:.2f} Pontos.", delta=f"{variacao_gap_percentual:.2f}%")
        
    st.divider()
   
   # CONDICIONAL PARA DEFINIR PONTUAÇÃO E PERCENTUAIS DE VARIAÇÃO DO DIA:
    if variacao_percentual >= 0:
        st.metric(label="Variação do dia: ", value=f"{variacao_dia_pontos:.2f} Pontos.", delta=f"{variacao_percentual:.2f}%")
    else:
        st.metric(label="Variação do dia: ", value=f"{variacao_dia_pontos:.2f} Pontos.", delta=f"{variacao_percentual:.2f}%")
    st.divider()
    
    
    pontuacao_maxima_dia = (maxima_dia - preco_ultimo_fechamento)
    percentual_maxima_dia =  (pontuacao_maxima_dia / preco_ultimo_fechamento) * 100
    
    pontuacao_minima_dia = (minima_dia - preco_ultimo_fechamento )
    percentual_minima_dia =  (pontuacao_minima_dia / preco_ultimo_fechamento) * 100


with st.sidebar:
    st.header('Variações:')
    
    # CONDITIONAL DE MÁXIMA:
    if percentual_maxima_dia >= 0:
        st.metric(label="Variação Máxima Positiva do dia: ", value=f"{pontuacao_maxima_dia:.2f} Pontos.", delta=f"{percentual_maxima_dia:.2f}%")
    
    else:
        st.write(':green[Sem dados de Máxima no momento...]')    
    
    # CONDITIONAL DE MÍNIMA:
    if percentual_minima_dia <= 0:    
        st.metric(label="Variação Mínima Negativa do dia: ", value=f"{pontuacao_minima_dia:.2f} Pontos.", delta=f"{percentual_minima_dia:.2f}%")
        
    else:
        st.write(':red[Sem dados de Mínima no momento...]')
          
    st.divider()

# Gráfico interativo do Nasdaq com Plotly:
fig = go.Figure(data=[go.Candlestick(x=dados_historico_intraday.index,
                open=dados_historico_intraday['Open'],
                high=dados_historico_intraday['High'],
                low=dados_historico_intraday['Low'],
                close=dados_historico_intraday['Close'])])

# Adicionando linhas de desvio padrão do DataFrame df_dp e anotações de texto
for index, row in df_dp.iterrows():
    color = 'green' if row['VALOR POR DP'] > 0 else 'red'  # Cor baseada no valor do desvio padrão
    preco_dp = preco_ultimo_fechamento + row['VALOR POR DP']
    descricao_dp = f'DP {row["DESVIOS PADRÕES"]}: {preco_dp:.2f}'
    
    # Adiciona a linha de desvio padrão
    fig.add_hline(y=preco_dp, line=dict(color=color, width=2, dash='dash'), name=descricao_dp)
    
    # Adiciona anotação de texto acima da linha de desvio padrão
    fig.add_annotation(xref='paper', x=0.95, y=preco_dp,
                       text=descricao_dp,
                       showarrow=False,
                       font=dict(family="Courier New, monospace",
                                 size=12,
                                 color=color),
                       align="right",
                       yshift=10)  # Ajuste vertical da anotação para não sobrepor a linha
    


# Adicionando linha e anotação de texto acima da linha do último fechamento:
fig.add_hline(preco_ultimo_fechamento, line=dict(color='blue', width=2, dash='dash'), name=f'Último Fechamento: {preco_ultimo_fechamento:.2f}')
descricao_ultimo_fechamento = (f'Fech. Anterior: {preco_ultimo_fechamento:.2f}')
fig.add_annotation(xref='paper', x=0.95, y=preco_ultimo_fechamento,
                    text=descricao_ultimo_fechamento,
                    showarrow=False,
                    font=dict(family="Courier New, monospace",
                                size=12,
                                color="blue"),
                    align="right",
                    yshift=10)  # Ajuste vertical da anotação para não sobrepor a linha


# Adicionando linha e anotação de texto acima da linha do última abertura:
fig.add_hline(ultima_abertura, line=dict(color='white', width=2, dash='dash'), name=f'Última Abertura: {ultima_abertura:.2f}')
descricao_ultima_abertura = (f'Última Abertura: {ultima_abertura:.2f}')
fig.add_annotation(xref='paper', x=0.95, y=ultima_abertura,
                    text=descricao_ultima_abertura,
                    showarrow=False,
                    font=dict(family="Courier New, monospace",
                                size=12,
                                color="white"),
                    align="right",
                    yshift=10)  # Ajuste vertical da anotação para não sobrepor a linha


# Adicionando linha e anotação de texto acima da linha do último Preço:
fig.add_hline(ultimo_preco, line=dict(color='#A020F0', width=2, dash='dash'), name=f'Última Preço: {ultimo_preco:.2f}')
descricao_ultimo_preco = (f'Último Preço: {ultimo_preco:.2f}')
fig.add_annotation(xref='paper', x=0.95, y=ultimo_preco,
                    text=descricao_ultimo_preco,
                    showarrow=False,
                    font=dict(family="Courier New, monospace",
                                size=12,
                                color="#A020F0"),
                    align="right",
                    yshift=10)  # Ajuste vertical da anotação para não sobrepor a linha


fig.add_vline(inicio_marcacao, name=('Início dia atual'), line=dict(color='yellow'))
fig.add_vline(final_marcacao, name=('Término dia atual'), line=dict(color='yellow'))
fig.update_layout(title=f"GRÁFICO INTRADIÁRIO DO {nome_ativo} ({sigla_ativo}), {pregao_atual}", xaxis_title='Data Histórico', yaxis_title='Preço Ativo', template = 'plotly_dark', title_x=0.25, title_font_color="#00FFFF", title_font_family="Times New Roman")
fig.update_layout(xaxis_rangeslider_visible=False)
fig.update_layout(height=720, width=1080)
fig.update_xaxes(title_font_family="Times New Roman", title_font_color="#00FF00")
fig.update_yaxes(title_font_family="Times New Roman", title_font_color="#00FF00")


# CRIANDO CONTAINER COM GRÁFICO INTERATIVO E MODELO DE CARREGAMENTO:
with st.container():
    with st.spinner('Aguarde por favor...'):
        time.sleep(10)
        
    
    st.success('Carregamento concluído com sucesso!')


    st.header('Gráfico Interativo:', divider='rainbow')
    st.plotly_chart(fig)
    
    # CRIANDO LEGENDAS ABAIXO DO GRÁFICO:
    with st.container():
        st.subheader('Lengenda Gráfico:')
        st.markdown(':red[Linhas Vermelhas: Pontos de VENDAS e possíveis PULLBACKS !]')
        st.markdown(':green[Linhas Verdes: Pontos de COMPRAS e possíveis PULLBACKS !]')
        st.markdown(':blue[Linha Azul: Último Fechamento !]')
        st.markdown(':violet[Linha Violeta: Último Preço !]')
        st.markdown(':white[Linha Branca: Última Abertura !]')
    
    st.divider()

coluna_1, coluna_2 = st.columns(2, gap='large')

# Adicionando Container do Gráfico Estático:
with st.container():
    with coluna_1:
    
        st.subheader('Tabela de Dados Intraday:', divider='rainbow')
        st.dataframe(dados_historico_intraday, height=520, width=520)
         
        
with st.container():      
    with coluna_2:
        st.subheader('Níveis de Desvios Padrões:', divider='rainbow')
        st.dataframe(df_dp, height=520, width=520)
        
    
with st.container(): 
    st.subheader('Tabela de Dados do Vencimento:', divider='rainbow')
    st.dataframe(dados_historico_vencimento, height=520, width=740)    
    
st.divider() 

fig.update_layout()
