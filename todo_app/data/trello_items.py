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
    
    query = {
        'key': api_key,
        'token': token
    }

    response = requests.request("GET", url, headers=headers, params=query)

    return response

def get_items():  
    reqUrl = "https://api.trello.com/1/boards/{0}/lists?cards=open".format( board_id)

    response = get_from_trello(reqUrl)
    response_json = response.json()

    cards = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            cards.append(card)

    return cards

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