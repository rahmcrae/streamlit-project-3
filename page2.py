import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from page1 import *

def show():
    st.write("This is Page 2")
    
    # Split the data into training and testing datasets
    X_train, X_test, y_train, y_test = train_test_split(df.index, df[plot_data_select], test_size=0.2, shuffle=False)

    # Convert the training and testing datasets into 2D arrays
    X_train = X_train.reshape(-1, 1)
    X_test = X_test.reshape(-1, 1)
    y_train = y_train.reshape(-1, 1)
    y_test = y_test.reshape(-1, 1)
    
    # Train the linear regression model
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Make predictions on the testing data
    y_pred = regressor.predict(X_test)

    # Calculate the mean squared error
    mse = mean_squared_error(y_test, y_pred)

    # Plot the actual vs predicted values
    st.line_chart(df[plot_data_select], y=plot_data_select)
    st.line_chart(y_pred, y=plot_data_select)

    st.write("Mean Squared Error: ", mse)