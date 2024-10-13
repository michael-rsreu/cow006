import typing

from src.card import Card

class Hand:
    def __init__(self, cards:  list[Card] = None):
        if cards is None:
            #для пустой руки
            cards = []
        self.cards: list[Card] = cards

    def __repr__(self):
        return self.save()

    def __eq__(self, other):
        if isinstance(other, str):
            other = Hand.load(other)
        return self.cards == other.cards

    def save(self) -> str:
        """Сохранение колоды в виде строки"""
        scards = [c.save() for c in self.cards]
        s = ' '.join(scards)
        return s

    @classmethod
    def load(cls, text: str) -> typing.Self:
        """Создание списка карт из строки"""
        cards = [Card.load(s) for s in text.split()]
        return cls(cards=cards)

    def add_card(self, card: Card):
        return self.cards.append(card)

    def remove_card(self, card: Card):
        return self.cards.remove(card)

    def score(self) -> int:
        return sum(c.score() for c in self.cards)