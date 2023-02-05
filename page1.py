import streamlit as st
import pandas as pd
import pandas_datareader as pdr
import os
import datetime

# Import the dataframe of tickers from the tickers.py file
from tickers import symbols

# set variables
api_key = os.getenv('TIINGO_API_KEY')
api_provider = "tiingo"


def show():
    st.write("This is Page 1")
    
    # select a ticker
    ticker = st.selectbox("select a ticker", symbols)
    
    # Select a start date
    start_date = st.date_input('select a start date', datetime.date(2011,1,1))
    
    # Select the data to plot
    plot_data = st.selectbox("Select the data to plot", ["open", "high", "low", "close","volume"])
    plot_data_select = str(plot_data)
    plot_data_select = plot_data_select.lower()
    
    if st.button("Submit"):
        # read data into dataframe
        df = pdr.DataReader(ticker, api_provider, start_date, api_key=api_key).reset_index()
        df['date'].dt.date  
        df.set_index('date',inplace=True)
        
        # plot a line chart & table of the selected data         
        st.line_chart(df[plot_data_select], y=plot_data_select)
        st.write(df.head(100))