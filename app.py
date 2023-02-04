import streamlit as st
import requests
from mailchimp_variables import *
from mongdb_variables import * 

def form():
    first_name = st.text_input("Enter your first name:")
    last_name = st.text_input("Enter your last name:")
    email = st.text_input("Enter your email:")
    password = st.text_input("Enter your password:", type='password')
    remember_me = st.checkbox("Remember me")

    if st.button("Submit"):        
        st.write("First Name: ", first_name)
        st.write("Last Name: ", last_name)
        st.write("Email: ", email)
        st.write("Password: ", password)
        st.write("Remember me: ", remember_me)
        inputs = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "remember_me": remember_me
        }        
                
        data = {
            "email_address": email,
            "merge_fields": {
            "FNAME": first_name,
            "LNAME": last_name
            },
            "status": "subscribed"
        }
        response = requests.post(url, headers=headers, json=data)
        
        # this logic will only submit to database if status code is successful
        if response.status_code == 200:
            collection.insert_one(inputs)
            st.success("Form submitted successfully - Thanks for subscribing!")            
        if response.status_code == 400 or response.status_code == 404:
            st.error("Form not submitted - Email already exists")
            return           

if __name__ == "__main__":
    form()