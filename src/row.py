from src.card import Card

class Row:

    def __init__(self):
        self.cards: list[Card] = []

    def __repr__(self):
        return ' '.join(repr(card) for card in self.cards)

    def add_card(self, card: Card):  # Метод такой же, что и в классе Hand. Просто добавляет в ряд карту без проверки условия.
        return self.cards.append(card)

    def has_max_lengh(self) -> bool:
        return len(self.cards) == 6

    def truncate(self):
        self.cards.clear()

    def can_play_on(self, card: Card) -> bool:
        if not self.cards:   # Есть ли вообще карта в ряду?
            self.cards.append(card)
            return True
        else:
            if card.can_play_on(self.cards[-1]):     # Меньше ли номинал карты, которую хотим положить?
                self.cards.append(card)
                return True