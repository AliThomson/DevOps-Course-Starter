import os

class TrelloService():
    def __init__(self):
        self.api_key = os.getenv('TRELLO_API_KEY')
        self.token = os.getenv('TRELLO_API_TOKEN')
        self.board_id = os.getenv('TRELLO_BOARD_ID')
        self.todo_list_id = os.getenv('TRELLO_TODO_LIST_ID')
        self.done_list_id = os.getenv('TRELLO_DONE_LIST_ID')
