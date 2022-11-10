import pymongo
import os

#MONGO_DB_URL = "mongodb+srv://vaasu:*************@cluster0.wydi0u7.mongodb.net/?retryWrites=true&w=majority"

import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:

        self.client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca) # client to communicate with mongodb server
        self.db_name="SensorData" # database name

    def insert_many(self,collection_name,records:list): # To perform batch insertion
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record): # To insert single record
        self.client[self.db_name][collection_name].insert_one(record)
        
