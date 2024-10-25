import pytest
import mongomock
from dotenv import find_dotenv, load_dotenv
from flask_dance.consumer.storage import MemoryStorage

from todo_app import app
from todo_app.classes.mongodb_service import MongoDbService
from todo_app.oauth import blueprint

@pytest.fixture
def client():
    storage = MemoryStorage({"access_token": "fake-token"})
    
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        setattr(blueprint, 'storage', storage)
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

def test_index_page(client):
    # Arrange
    mongoDbService = MongoDbService()

    test_document = {
        "name": "Test item",
        "status": "To do"
    }

    mongoDbService.todo_items.insert_one(test_document)

    # Act
    response = client.get('/')


    # Assert
    assert response.status_code == 200
    assert "Test item" in response.data.decode()