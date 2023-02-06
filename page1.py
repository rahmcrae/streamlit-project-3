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
             ### One Stock Analysis
             """)
    
    # select a start date
    #start_date = st.date_input('select a start date', date(1900,1,1))
    # min & max dates for slider
    min_date = date(1900,1,1)
    max_date = date.today()
    
    # date range slider    
    date_range = st.slider('select date range', min_value=min_date, max_value=max_date, label_visibility="visible", value=(min_date,max_date))
    date_range_list = list(date_range)          
    
    # select a ticker
    ticker = st.selectbox("select a ticker", symbols)
    
    # select the data to plot
    plot_data = st.selectbox("select the data to plot", ["Open", "High", "Low", "Close","Volume"])
    plot_data_select = str(plot_data)
    
    if st.button("Submit"):
        # read data into dataframe
        
        try:
            df = pd.DataFrame(yf.download(ticker, start=date_range_list[0], end=date_range_list[1], group_by='ticker')).reset_index()            
                        
        except ValueError:
            st.error("Data doesn't exist for the selected date range.") 
            
        else:
            df.set_index('Date',inplace=True)
            #df.index = df.index.date
            df.index = [d.date() for d in df.index]

            # plot a line chart & table of the selected data         
            st.line_chart(df[plot_data_select], y=plot_data_select)
            st.write(df.head(len(df)).sort_index(ascending=False))