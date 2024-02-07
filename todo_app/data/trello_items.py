import os
import requests
import json

api_key = os.getenv('TRELLO_API_KEY')
token = os.getenv('TRELLO_API_TOKEN')
board_id = os.getenv('TRELLO_BOARD_ID')
list_id = os.getenv('TRELLO_LIST_ID')

def get_from_trello(url):
    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
    }
    payload = ""

    response = requests.request("GET", url, data=payload,  headers=headersList)

    print(response.text)
    return response

def get_items():
    
    reqUrl = "https://api.trello.com/1/boards/{board_id}/lists?cards=open&card_fields=name&fields=name&key={api_key}&token={token}"

    response = get_from_trello(reqUrl)
    response_json = response.json()

    cards = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            cards.append(card)

    return cards
# def get_items():
    
#     reqUrl = "https://api.trello.com/1/lists/{list_id}/cards?fields=name&key={api_key}&token={token}"

#    return get_from_trello(reqUrl)

def add_item(name):
    reqUrl = "https://api.trello.com/1/cards?idList={list_id}&key={api_key}&token={token}"

    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Content-Type": "application/json" 
    }

    payload = json.dumps({
    "name": name,
    "pos": "bottom"
    })

    response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

    print(response.text)