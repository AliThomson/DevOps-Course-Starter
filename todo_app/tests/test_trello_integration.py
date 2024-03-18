import pytest
from dotenv import find_dotenv, load_dotenv
import requests


from todo_app import app
from todo_app.classes.trello_service import TrelloService
from todo_app.data.trello_items import get_cards



@pytest.fixture
def client():
    file_path = find_dotenv('.env.test.')
    load_dotenv(file_path, override=True)

    test_app = app.create_app()

    with test_app.test_client() as client:
        yield client

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data
    
def stub(url, params={}, headers={}):
    testTrello = TrelloService()
    test_board_id = testTrello.board_id

    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists?cards=open&card_fields=id,name&fields=name':
        fake_response_data = [{
            'id': '1',
            'name': 'To Do',
            'cards': [{'id': '456', 'name': 'Test card'}]
        }]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')

def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'get', stub)

    response = client.get('/')

    assert response.status_code == 200
    assert 'Test card' in response.data.decode()