import pymongo
import os

class MongoDbService():
    def __init__(self):
        client = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_STRING"))
        db = client[os.getenv("MONGODB_NAME")]
        self.todo_items = db[os.getenv("MONGODB_COLLECTION_NAME")]
