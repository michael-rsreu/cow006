import json
from src.card import Card
from src.row import Row
from src.player import Player

class Table:
    def __init__(self):
        self.rows: list[Row] = [Row() for _ in range(4)]        # Ряды имеют номера от 0 до 3
        self.select_cards: list[tuple[Player, Card]] = []       # Инициализация списка карт, которые выбрали игроки

    def __repr__(self):
        repr_rows = [f"row{i + 1}: {repr(row)}" for i, row in enumerate(self.rows)]
        return "\n".join(repr_rows)

    def __getitem__(self, item):
        return self.rows[item]

    def add_card(self, card: Card) -> bool:
        good_rows = []   # Список рядов, в которых номер карты меньше чем номер выбранной

        for row in self.rows:               # Проверка, что номер выбранной больше
            if row.can_play_on(card):
                good_rows.append(row)

        if not good_rows:       # Если ни один ряд не подходит
            return False

        best_row = min(good_rows, key=lambda r: abs(card.number - r.cards[-1].number))      # Ряд с наименьшей разницей

        if len(best_row.cards) == Row.MAX_LEN - 1:          # Если карта шестая в ряду
            print(f'Игрок забрал ряд {self.rows.index(best_row) + 1}')
            best_row.truncate()

        best_row.add_card(card)         # Шестая карта становится первой в ряду
        return True

    def save(self) -> str:
        return json.dumps({f"row{i + 1}": self.rows[i].save() for i in range(len(self.rows))})

    @classmethod
    def load(cls, data: dict) -> 'Table':
        table = cls()
        for row_key, cards_str in data.items():
            row = Row.load(cards_str)
            row_index = int(row_key.replace("row", "")) - 1
            table.rows[row_index] = row
        return table