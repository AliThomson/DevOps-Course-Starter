import os
import requests
import json

api_key = os.getenv('TRELLO_API_KEY')
token = os.getenv('TRELLO_API_TOKEN')
board_id = os.getenv('TRELLO_BOARD_ID')
list_id = os.getenv('TRELLO_LIST_ID')

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

def get_items():  
    reqUrl = "https://api.trello.com/1/boards/{0}/lists?cards=open&card_fields=id,name&fields=name".format(board_id)

    response = get_from_trello(reqUrl)
    response_json = response.json()

    cards = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            card['status'] = trello_list['name']
            cards.append(card)

    return cards

def add_item(new_task_name):
    reqUrl = "https://api.trello.com/1/cards?idList={0}".format(list_id)

    response = post_to_trello(reqUrl, new_task_name)

    print(response.text)