from todo_app.classes.card import Card
from todo_app.classes.view_model import ViewModel

# Arrange
test_cards = []
test_cards.append(Card(1, "test1", "To Do"))
test_cards.append(Card(2, "test2", "Doing"))
test_cards.append(Card(3, "test3", "Doing"))
test_cards.append(Card(4, "test4", "Done"))
test_cards.append(Card(5, "test5", "Done"))
test_cards.append(Card(6, "test6", "Done"))

test_view_model = ViewModel(test_cards)

def test_view_model_done_property():

# Act
    result = test_view_model.done_cards

# Assert
    assert len(result) == 3
    assert result[0].name == "test4"

def test_view_model_doing_property():

# Act
    result = test_view_model.doing_cards

# Assert
    assert len(result) == 2
    assert result[0].name == "test2"

def test_view_model_doing_property():

# Act
    result = test_view_model.to_do_cards

# Assert
    assert len(result) == 1
    assert result[0].name == "test1"