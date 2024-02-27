import requests
import json

from todo_app.classes.card import Card
from todo_app.classes.trello_service import TrelloService

myTrello = TrelloService()

def get_from_trello(url):
    headers = {
        "Accept": "application/json"
    }
    
    auth_data = {
        "key": myTrello.api_key,
        "token": myTrello.token
    }

    response = requests.get(url, headers=headers, params=auth_data)

    return response

def post_to_trello(url, new_task_name):   
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "key": myTrello.api_key,
        "token": myTrello.token,
        "name": new_task_name,
        "pos": "bottom"
    })
   
    response = requests.post(url, headers=headers, data=payload)

    return response

def update_item_list(url, new_list_id):   
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "key": myTrello.api_key,
        "token": myTrello.token,
        "idList": new_list_id,
        "pos": "bottom"
    })
   
    return requests.put(url, headers=headers, data=payload)

def get_items():  
    reqUrl = f"https://api.trello.com/1/boards/{myTrello.board_id}/lists?cards=open&card_fields=id,name&fields=name"

    response = get_from_trello(reqUrl)
    board = response.json()

    cards = []
    for list in board:
        for card in list['cards']:
            cards.append(Card.from_trello_board(card, list))

    return cards

def add_item(new_task_name):
    reqUrl = f"https://api.trello.com/1/cards?idList={myTrello.todo_list_id}"

    return post_to_trello(reqUrl, new_task_name)

def move_item(item_id, new_list):
    reqUrl = f"https://api.trello.com/1/cards/{item_id}"
    if new_list == "todo":
        new_list_id = myTrello.todo_list_id
    else:
        new_list_id = myTrello.done_list_id

    return update_item_list(reqUrl, new_list_id)
