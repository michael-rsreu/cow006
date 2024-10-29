from src.card import Card

class Row:

    MAX_LEN = 6

    def __init__(self):
        self.cards: list[Card] = []

    def __repr__(self):
        return ' '.join(card.__str__() for card in self.cards)

    def add_card(self, card: Card):
        return self.cards.append(card)

    def has_max_lengh(self) -> bool:
        return len(self.cards) == self.MAX_LEN

    def truncate(self):
        self.cards.clear()

    def can_play_on(self, card: Card) -> bool:
        return not self.cards or card.can_play_on(self.cards[-1])

    def save(self) -> str:
        return ' '.join(card.save() for card in self.cards)

    @staticmethod
    def load(data: str) -> 'Row':
        row = Row()
        list_cards = data.split(' ')
        for card in list_cards:
            row.add_card(Card.load(card))
        return row