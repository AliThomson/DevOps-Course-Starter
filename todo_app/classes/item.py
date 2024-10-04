class Item:
    def __init__(self, id, name, status = 'To do'):
        self.id = id
        self.name = name
        self.status = status
    
    @classmethod
    def from_mongo_document(cls, document):
        return cls(document['_id'], document['name'], document['status'])