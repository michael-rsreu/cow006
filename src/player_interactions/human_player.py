from src.card import Card
from src.hand import Hand
from src.table import Table

from src.player_interaction import PlayerInteraction

class Human(PlayerInteraction):

    @classmethod
    def choose_card(cls, hand: Hand, table: Table, hand_counts: list[int] | None = None) -> Card:
        """Выбор карты игроком и ввод"""
        while True:
            try:
                print('Карты в руке: ', hand)
                card_text = int(input('Выберите карту: '))
                for card in hand.cards:
                    if card.number == card_text:
                        return card
                else:
                    print('Этой карты нет в руке')
            except ValueError:
                print('Карта указана в неверном формате. Повторите ввод.')

    @classmethod
    def choose_row(cls, table: Table, card: Card) -> int:
        """Выбор ряда игроком и ввод"""
        while True:
            try:
                row_text = int(input("Выберете ряд, который заберете (1-4): ")) - 1
                if 0 <= row_text < len(table.rows):
                    print(f"\tВыбрал ряд {row_text+1}")
                    return row_text
                else:
                    print("Повторите ввод. Введите число, указывающее на номер ряда ")
            except ValueError:
                print("Повторите ввод. Введите число, указывающее на номер ряда ")