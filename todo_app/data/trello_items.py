import os
import requests
import json

from todo_app.classes.card import Card

api_key = os.getenv('TRELLO_API_KEY')
token = os.getenv('TRELLO_API_TOKEN')
board_id = os.getenv('TRELLO_BOARD_ID')
todo_list_id = os.getenv('TRELLO_TODO_LIST_ID')
done_list_id = os.getenv('TRELLO_DONE_LIST_ID')

def get_from_trello(url):
    headers = {
        "Accept": "application/json"
    }
    
    auth_data = {
        "key": api_key,
        "token": token
    }

    response = requests.get(url, headers=headers, params=auth_data)

    return response

def post_to_trello(url, new_task_name):   
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "key": api_key,
        "token": token,
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
        "key": api_key,
        "token": token,
        "idList": new_list_id,
        "pos": "bottom"
    })
   
    return requests.put(url, headers=headers, data=payload)

def get_items():  
    reqUrl = f"https://api.trello.com/1/boards/{board_id}/lists?cards=open&card_fields=id,name&fields=name"

    response = get_from_trello(reqUrl)
    board = response.json()

    cards = []
    for list in board:
        for card in list['cards']:
            cards.append(Card.from_trello_board(card, list))

    return cards

def add_item(new_task_name):
    reqUrl = f"https://api.trello.com/1/cards?idList={todo_list_id}"

    return post_to_trello(reqUrl, new_task_name)

def move_item(item_id, new_list):
    reqUrl = f"https://api.trello.com/1/cards/{item_id}"
    if new_list == "todo":
        new_list_id = todo_list_id
    else:
        new_list_id = done_list_id

    return update_item_list(reqUrl, new_list_id)
