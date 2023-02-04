import streamlit as st
import requests
from mongdb_variables import *
import page1
import page2
import page3

def main():
    st.write("""
             # Analysis Project
             ### By: Rah McRae
             The purpose of this is to analyze x,y,z over time.
             """)        
    # Create a navigation menu
    menu = ["Page 1", "Page 2", "Page 3"]
    choice = st.sidebar.selectbox("Select a page", menu)

    # Show the selected page
    if choice == menu[0]:
        page1.show()
    elif choice == menu[1]:
        page2.show()
    elif choice == menu[2]:
        page3.show()        
    return           

if __name__ == "__main__":
    main()