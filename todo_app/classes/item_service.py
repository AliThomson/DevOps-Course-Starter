from bson import ObjectId

from todo_app.classes.item import Item
from todo_app.classes.mongodb_service import MongoDbService
from flask import current_app

class ItemService:
    def __init__(self):
        self.mongoDbService = MongoDbService()

    def get_items(self):
        mongo_documents = list(self.mongoDbService.todo_items.find())
        
        items = []
        for document in mongo_documents:
            item = Item.from_mongo_document(document)
            items.append(item)

        return items

    def add_item(self, new_task_name: str):
        
        new_item = {
            "name": new_task_name,
            "status": "To do"
        }
        self.mongoDbService.todo_items.insert_one(new_item)
        current_app.logger.info(f"Successfully added item: {new_item} in db")

    def update_item(self, item_id: str, status: str):
        self.mongoDbService.todo_items.update_one({"_id": ObjectId(item_id)}, {"$set": {"status": status}})
        current_app.logger.info("Successfully updated item: {item_id} to {status} in db")

