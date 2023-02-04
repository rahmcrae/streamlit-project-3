from pymongo import MongoClient
from mailchimp_variables import *

client = MongoClient("mongodb://localhost:27017/")
db = client["forms"]
collection = db["subscribers"]

headers = {
            "Authorization": f"apikey {api_key}",
            "Content-Type": "application/json"
        }