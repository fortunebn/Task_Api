import os
from dotenv import load_dotenv
from pymongo import mongo_client

load_dotenv()

MONGO_DB_URL = os.environ.get("MONGO_DB_URL")
Client = mongo_client.MongoClient(MONGO_DB_URL)

User_Collection = Client["TaskAPI"]["User"]
Task_Collection = Client["TaskAPI"]["Task"]