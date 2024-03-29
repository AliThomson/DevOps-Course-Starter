class Card:
    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_board(cls, card, list):
        return cls(card['id'], card['name'], list['name'])