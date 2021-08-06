import yfinance as yf
import streamlit as st
import pandas as pd
from get_all_tickers import get_tickers as gt

tick = pd.read_csv("tickers.csv", names='t')
list_of_tickers = list(tick['t'])

make_choice = st.sidebar.selectbox('Select your ticker:', list_of_tickers)

st.write("""
## Stock Price APP

Shown are the stock **closing price** and **volume** of your choice!
***
""")


# defining the ticker symbol
tickerSymbol = make_choice
# get data for this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2010-08-04', end='2021-08-04')
# open high low close volume dividents stocksplits



st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)

st.write("""

Blitz

""")