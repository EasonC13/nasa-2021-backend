from dotenv import load_dotenv
import os
load_dotenv(".env")

MONGODB_URL = os.getenv("MONGODB_URL", 27017)

from pymongo import MongoClient

client = MongoClient("mongodb://NASA2021:NASA2021SEALNO1@e3.pc.eason.tw:27017")

db = client['NASA2021']
