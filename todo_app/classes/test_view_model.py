from todo_app.classes.card import Card
from todo_app.classes.view_model import ViewModel


def test_view_model_done_property():
# Arrange
    done_cards = []
    done_cards.append(Card(1, "test1", "Done"))
    done_cards.append(Card(2, "test2", "Done"))
    done_cards.append(Card(3, "test3", "Done"))

    done_cards_view_model = ViewModel(done_cards)

# Act
    result = done_cards_view_model.done_cards

# Assert
    assert len(result) == 3
    assert result[0].name == "test1"