from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["streamlit"]
collection = db["streamlit-project-3"]