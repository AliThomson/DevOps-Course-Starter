class ViewModel:
    def __init__(self, cards):
        self._cards = cards

    @property
    def cards(self):
        return self._cards
    
    @property
    def done_cards(self):
        return []