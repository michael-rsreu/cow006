from src.card import Card
from src.row import Row
from src.hand import Hand
from src.table import Table
from src.player import Player
from src.player_interaction import PlayerInteraction
from random import randint, choice

class Bot(PlayerInteraction):

    @classmethod
    def choose_card(cls, hand: Hand, table: Table, hand_counts: list[int] | None = None) -> Card:
        """Выбор карты ботом и ввод"""
        chosen_card = choice(hand.cards)
        return chosen_card

    @classmethod
    def choose_row(cls, table: Table, card: Card) -> int:
        """Выбор ряда ботом и ввод"""
        chosen_row = randint(0, len(table.rows) - 1)
        print(f"Бот выбрал ряд {chosen_row+1}")
        return chosen_row

    @classmethod
    def inform_card_chosen(cls, player: Player):
        """
        Сообщает, что игрок выбрал карту.
        """
        pass

    @classmethod
    def inform_row_chosen(cls, player: Player, row: int):
        """
        Сообщает, что игрок выбрал ряд.
        """
        pass