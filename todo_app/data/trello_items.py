import requests

from todo_app.classes.card import Card
from todo_app.classes.trello_service import TrelloService


def update_item_list(url, new_list_id):   
    trelloService = TrelloService()
    
    payload = trelloService.put_to_trello(new_list_id)
   
    return requests.put(url, headers=trelloService.headers, data=payload)

def get_cards():  
    trelloService = TrelloService()
    reqUrl = f"https://api.trello.com/1/boards/{trelloService.board_id}/lists?cards=open&card_fields=id,name&fields=name"

    auth_data = trelloService.get_from_trello()
    response = requests.get(reqUrl, headers=trelloService.headers, params=auth_data)

    board = response.json()

    cards = []
    for list in board:
        for card in list['cards']:
            cards.append(Card.from_trello_board(card, list))

    return cards

def add_card(new_task_name):
    trelloService = TrelloService()
    reqUrl = f"https://api.trello.com/1/cards?idList={trelloService.todo_list_id}"
    
    add_card_data = trelloService.post_to_trello(new_task_name)

    return requests.post(reqUrl, headers=trelloService.headers, data=add_card_data)

def move_card(item_id, new_list):
    trelloService = TrelloService()
    reqUrl = f"https://api.trello.com/1/cards/{item_id}"
    if new_list == "todo":
        new_list_id = trelloService.todo_list_id
    else:
        new_list_id = trelloService.done_list_id

    return update_item_list(reqUrl, new_list_id)
