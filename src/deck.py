import random
import typing

from src.card import Card

class Deck:

    def __init__(self, cards: None | list[Card]):
        if cards is None:
            # создание новой колоды
            cards = Card.all_cards()
            random.shuffle(cards)
        self.cards: list[Card] = cards

    def __repr__(self):
        return self.save()

    def __eq__(self, other):
        return self.cards == other.cards

    def shuffle(self):
        """Перемешивание карт"""
        random.shuffle(self.cards)

    @classmethod
    def load(cls, text: str) -> typing.Self:
        """Создание списка карт из строки"""
        cards = [Card.load(s) for s in text.split()]
        return cls(cards=cards)

    def save(self) -> str:
        """Сохранение колоды в виде строки"""
        scards = [c.save() for c in self.cards]
        s = ' '.join(scards)
        return s

    def draw_card(self):
        """Берем карту из колоды и возвращаем ее."""
        return self.cards.pop()