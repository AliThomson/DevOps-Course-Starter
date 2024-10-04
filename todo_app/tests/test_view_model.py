import pytest
from todo_app.classes.item import Item
from todo_app.classes.view_model import ViewModel

# Arrange
@pytest.fixture
def test_view_model():
    test_cards = []
    test_cards.append(Item(1, "test1", "To do"))
    test_cards.append(Item(2, "test2", "Doing"))
    test_cards.append(Item(3, "test3", "Doing"))
    test_cards.append(Item(4, "test4", "Done"))
    test_cards.append(Item(5, "test5", "Done"))
    test_cards.append(Item(6, "test6", "Done"))

    return ViewModel(test_cards)

def test_view_model_done_property(test_view_model):

# Act
    result = test_view_model.done_cards

# Assert
    assert len(result) == 3
    assert any(card.name == "test4" for card in result)

def test_view_model_doing_property(test_view_model):

# Act
    result = test_view_model.doing_cards

# Assert
    assert len(result) == 2
    assert any(card.name == "test2" for card in result) 

def test_view_model_to_do_property(test_view_model):

# Act
    result = test_view_model.to_do_cards

# Assert
    assert len(result) == 1
    assert any(card.name == "test1" for card in result)