class Item:
    def __init__(self, id, name, status = 'To do'):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_board(cls, card, list):
        return cls(card['id'], card['name'], list['name'])
    
    @classmethod
    def from_mongo_document(cls, document):
        return cls(document['_id'], document['name'], document['status'])