class ViewModel:
    def __init__(self, cards):
        self._cards = cards

    @property
    def cards(self):
        return self._cards
    
    @property
    def done_cards(self):
        return [card for card in self.cards if card.status == "Done"]
    
    @property
    def doing_cards(self):
        return [card for card in self.cards if card.status == "Doing"]
    
    @property
    def to_do_cards(self):
        return [card for card in self.cards if card.status == "To Do"]