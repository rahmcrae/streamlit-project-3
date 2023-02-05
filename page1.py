import streamlit as st
import pandas as pd
import pandas_datareader as pdr
import os
from datetime import *
import yfinance as yf

# Import the dataframe of tickers from the tickers.py file
from tickers import symbols

#set variables
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def show():
    st.write("This is Page 1")
    
    # select a ticker
    ticker = st.selectbox("select a ticker", symbols)
    
    # Select a start date
    start_date = st.date_input('select a start date', date(2000,1,1))
    
    # Select the data to plot
    plot_data = st.selectbox("select the data to plot", ["Open", "High", "Low", "Close","Volume"])
    plot_data_select = str(plot_data)
    
    # Select the # of rows for table
    number = st.slider("select the number of records for table",  min_value=None, max_value=None, value=None, step=10,label_visibility="visible")
    
    
    if st.button("Submit"):
        # read data into dataframe
        
        df = pd.DataFrame(yf.download(ticker, start=start_date, end=date.today(), group_by='ticker')).reset_index()
        df.set_index('Date',inplace=True)
        df.index = df.index.date
        
        # plot a line chart & table of the selected data         
        st.line_chart(df[plot_data_select], y=plot_data_select)
        st.write(df.head(number))
        
        if st.button("Download Data"):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # encode as base64
        href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)