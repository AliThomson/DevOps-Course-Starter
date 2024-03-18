import json
import os

class TrelloService():
    def __init__(self):
        self.api_key = os.getenv('TRELLO_API_KEY')
        self.token = os.getenv('TRELLO_API_TOKEN')
        self.board_id = os.getenv('TRELLO_BOARD_ID')
        self.todo_list_id = os.getenv('TRELLO_TODO_LIST_ID')
        self.done_list_id = os.getenv('TRELLO_DONE_LIST_ID')
        self.doing_list_id = os.getenv('TRELLO_DOING_LIST_ID')
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def get_from_trello(self):
        auth_data = {
            "key": self.api_key,
            "token": self.token
        }

        return auth_data

    def post_to_trello(self, new_task_name):
        payload = json.dumps({
            "key": self.api_key,
            "token": self.token,
            "name": new_task_name,
            "pos": "bottom"
        })
        
        return payload
    
    def put_to_trello(self, new_list_id):
        payload = json.dumps({
            "key": self.api_key,
            "token": self.token,
            "idList": new_list_id,
            "pos": "bottom"
        })
        
        return payload
