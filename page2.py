import streamlit as st
import pandas as pd
import os
from datetime import *
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Import the dataframe of tickers from the tickers.py file
from tickers import symbols

def show():
    st.write("""
             ### Multi- Select
             """)
    
    # select a ticker
    tickers = st.multiselect("select tickers", symbols, default='AAPL', label_visibility="visible", max_selections=5)
    
    # select a start date
    start_date = st.date_input('select a start date', date(2000,1,1))
    
    # select the data to plot
    plot_data = st.selectbox("select the data to plot", ["Open", "High", "Low", "Close","Volume"])
    plot_data_select = str(plot_data)
    
    # select the # of rows for table
    max_value = len(pd.DataFrame(yf.download(tickers, start=start_date, end=date.today(), group_by='ticker')).reset_index())
    number = st.slider("select the number of records for table",  min_value=None, max_value=max_value, value=None, step=10,label_visibility="visible")    
    
    if st.button("Submit"):
        # read data into dataframe
        
        dfs = [yf.download(ticker, start=start_date, end=date.today(), group_by='ticker') for ticker in tickers]
        df = pd.concat([df.assign(Ticker=ticker) for ticker, df in zip(tickers, dfs)])
        df = df.reset_index()
        #df = df.rename(columns={"Date": "date"})
        #df = pd.concat(dfs, axis=1, keys=tickers)
        df.set_index('Date',inplace=True)
        df.index = df.index.date
        
        # plot a line chart & table of the selected data
        #st.line_chart(df.groupby("date")["Close"].mean())         
        st.line_chart(df[plot_data_select], y=plot_data_select)
        st.write(df.head(number))
        st.write(print(df.head(number)))