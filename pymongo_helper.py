import pymongo
import dotenv
import os

dotenv.load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_STRING"))

db = client[os.getenv("MONGODB_NAME")]

todo_items = db[os.getenv("MONGODB_COLLECTION_NAME")]

item_one = {"description": "testing"}
item_two = {"description": "Updateable item", "type": "updateable"}
item_three = {"description": "Another updateable item", "type": "updateable"}

# INSERT a new item
item_id = todo_items.insert_one(item_three)

# UPDATE a new item
todo_items.update_one({"type": "updateable"}, {"$set": {"description": "Changed"}})

# SELECT all items
list(todo_items.find())

print(list(todo_items.find()))