import pymongo

from todo_app.classes.item import Item
from todo_app.classes.mongodb_service import MongoDbService

def get_items():
    mongoDbService = MongoDbService()
    mongo_documents = list(mongoDbService.todo_items.find())

    items = []
    for document in mongo_documents:
        item = Item.from_mongo_document(document)
        items.append(item)

    return items

def add_item(new_task_name: str):
    mongoDbService = MongoDbService()
    new_item = {
        "name": new_task_name,
        "status": "To do"
    }
    mongoDbService.todo_items.insert_one(new_item)

def update_item(item_id, status):
    pass
