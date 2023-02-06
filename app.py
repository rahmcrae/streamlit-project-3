import streamlit as st
import requests
from mongdb_variables import *
import page1
import page2
import page3

def main():
    st.write("""
             # 💸 Financial Derivatives Analysis 💸
             ## By: :red[Rah McRae]
             #### Purpose: :red[_to analyze different financial derivatives over time_]
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