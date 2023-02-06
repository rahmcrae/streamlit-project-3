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
             ### Multi-Stock Analysis (Max 5)
             """)
    
    # min & max dates for slider
    min_date = date(1900,1,1)
    max_date = date.today()
    
    # date range slider    
    date_range = st.slider('select date range', min_value=min_date, max_value=max_date, label_visibility="visible", value=(min_date,max_date))
    date_range_list = list(date_range)          
    
    # select tickers
    tickers = st.multiselect("select tickers", symbols, default='AAPL', label_visibility="visible", max_selections=5)
    
    # select the data to plot
    plot_data = st.selectbox("select the data to plot", ["Open", "High", "Low", "Close","Volume"])
    plot_data_select = str(plot_data)
    
    if st.button("Submit"):
        # read data into dataframe
        
        if not tickers:
            st.error("no ticker selected")
        else:    
            dfs = [yf.download(ticker, start=date_range_list[0], end=date_range_list[1], group_by='ticker') for ticker in tickers]
            df = pd.concat([df.assign(Ticker=ticker) for ticker, df in zip(tickers, dfs)])
            df = df.reset_index()
            df.set_index('Date',inplace=True)
            #df.index = df.index.date
            df.index = [d.date() for d in df.index]
            
            # plot a line chart & table of the selected data
            #st.line_chart(df.groupby("date")["Close"].mean())         
            st.line_chart(df[plot_data_select], y=plot_data_select)
            st.write(df.head(len(df)).sort_index(ascending=False))
            print(df.head(len(df)).sort_index(ascending=False))
