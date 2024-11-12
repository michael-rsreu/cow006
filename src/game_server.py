import enum
import inspect
import json

from src.deck import Deck
from src.game_state import GameState
from src.table import Table
from src.player import Player
from src.hand import Hand
from src.player_interaction import PlayerInteraction
import src.player_interactions as all_player_types

class GamePhase(enum.StrEnum):
    DEAL_CARDS = 'Deal cards'                                       # Фаза раздачи карт
    DISPLAY_TABLE = 'Display table state'                           # Фаза отображения состояния стола
    CHOOSE_CARD = 'Choose card'                                     # Выбор разыгрываемой карты
    CHOOSE_ROW = 'Choose row'                                       # Выбор забираемого ряда
    PLACE_CARD = 'Place card'                                       # Положить карту в ряд
    NEXT_PLAYER = 'Switch current player'                           # Передача хода другому игроку
    DECLARE_WINNER = 'Declare a winner'                             # Объявление победителя
    GAME_END = 'Game ended'                                         # Завершение игры
    FILL_TABLE = "Place cards on the table"                         # Разыгрываемая карта кладется на стол в закрытую


class GameServer:
    INITIAL_HAND_SIZE = 10                                          # Кол-во карт в руке и ходов
    chosen_cards = {}                                               # Вместо add_selected_card

    def __init__(self, player_types, game_state):
        self.game_state: GameState = game_state
        self.player_types: dict = player_types  # {player: PlayerInteractions}
        self.turn_number = 0

    @classmethod
    def load_game(cls):
        filename = 'cow006.json'
        with open(filename, 'r') as fin:
            data = json.load(fin)
            game_state = GameState.load(data)
            print(game_state.save())
            player_types = {}
            for player, player_data in zip(game_state.players, data['players']):
                kind = player_data['kind']
                kind = getattr(all_player_types, kind)
                player_types[player] = kind
            return GameServer(player_types=player_types, game_state=game_state)

    def save(self):
        filename = 'cow006.json'
        data = self.save_to_dict()
        with open(filename, 'w') as fout:
            json.dump(data, fout, indent=4)

    def save_to_dict(self):
        data = self.game_state.save()
        for player_index, player in enumerate(self.player_types.keys()):
            player_interaction = self.player_types[player]
            data['players'][player_index]['kind'] = self.player_types[player].__name__
        return data

    @classmethod
    def get_player(cls):
        player_count = cls.request_player_count()

        player_types = {}
        names_count = {}
        for _ in range(player_count):
            name, kind = cls.request_player()

            if name in names_count:
                names_count += 1
                uniq_name = name + str(names_count[name])
                print(f'Имя {name} изменено на {uniq_name}')
            else:
                names_count[name] = 1
                uniq_name = name

            player = Player(uniq_name, Hand())
            player_types[player] = kind
        return player_types

    @staticmethod
    def request_player_count() -> int:
        while True:
            try:
                player_count = int(input("Сколько всего игроков?"))
                if 2 <= player_count <= 10:
                    return player_count
            except ValueError:
                pass
            print("Пожалуйста, введите число от 2 до 10")

    @staticmethod
    def request_player() -> (str, PlayerInteraction):
        """Возвращает имя и тип игрока"""
        player_types = []

        for name, cls in inspect.getmembers(all_player_types):                                                          # Берет из PlayerInteractions все возможные типы игроков и преобразует в строку
            if inspect.isclass(cls) and issubclass(cls, PlayerInteraction):
                player_types.append(cls.__name__)
        player_types_as_str = ', '.join(player_types)

        while True:
            name = input("Как зовут игрока?")
            if name.isalpha():
                break
            print("Имя должно состоять из одного слова и только из букв")

        while True:
            try:
                kind = input(f"Кем является игрок ({player_types_as_str})?")
                kind = getattr(all_player_types, kind)
                break
            except AttributeError:
                print(f"Разрешенные типы игроков: {player_types_as_str}")

        return name, kind

    @classmethod
    def new_game(cls, player_types: dict):
        deck = Deck(cards=None)
        table = Table()
        for row in table:
            row.add_card(deck.draw_card())
        game_state = GameState(list(player_types.keys()), deck, table)

        res = cls(player_types, game_state)
        res.deal_cards_phase()
        return res


    def run(self):
        current_phase = GamePhase.DISPLAY_TABLE
        while current_phase != GamePhase.GAME_END:
            phases = {
                GamePhase.CHOOSE_CARD: self.choose_card_phase,
                GamePhase.DISPLAY_TABLE: self.display_table_state,
                GamePhase.DEAL_CARDS:  self.deal_cards_phase,
                GamePhase.PLACE_CARD: self.place_card_phase,
                GamePhase.NEXT_PLAYER: self.next_player_phase,
                GamePhase.DECLARE_WINNER: self.declare_winner_phase,
            }
            current_phase = phases[current_phase]()

    def inform_all(self, method: str, *args, **kwargs):
        for p in self.player_types.values():
            getattr(p, method)(*args, **kwargs)

    def choose_card_phase(self) -> GamePhase:
        current_player = self.game_state.current_player()
        card = self.player_types[current_player].choose_card(current_player.hand, self.game_state.table)
        self.inform_all('inform_card_chosen', {current_player})
        if card:
            self.chosen_cards[current_player] = card

        if len(self.chosen_cards) == len(self.player_types):            # Сколько игроков, столько карт выбрано
            return GamePhase.PLACE_CARD
        else:
            return GamePhase.NEXT_PLAYER

    def display_table_state(self):  # отображение состояние стола
        self.turn_number += 1
        if self.turn_number <= self.INITIAL_HAND_SIZE:
            print(f'\n----Ход №{self.turn_number}----\n'
                  f'Состояние стола: {self.game_state.table}\n'
                  f'Игроки выбирают по одной карте')
            return GamePhase.CHOOSE_CARD
        else:
            return GamePhase.GAME_END

    def deal_cards_phase(self) -> GamePhase:
        for _ in range(self.INITIAL_HAND_SIZE):
            for p in self.player_types.keys():
                p.hand.add_card(self.game_state.deck.draw_card())
        print("Карты разданы игрокам.")
        return GamePhase.DISPLAY_TABLE

    def place_card_phase(self):
        print("\n--- Раскрытие выбранных карт ---")
        for player, card in self.chosen_cards.items():
            print(f"{player.name}({player.score}): {card}")
        print("----------------------------------")

        for player, card in sorted(self.chosen_cards.items(), key=lambda x: x[1].number):
            print(f'{player.name}({player.score}): добавление карты {card}')
            try:
                try_play = self.game_state.play_card(card, player)
                if try_play:
                    print(f'Карта игрока {player.name}({player.score}) добавлена в один из рядов')
                else:
                    print(f"Карту игрока {player.name}({player.score}) невозможно добавить на стол")
                    row_index = self.player_types[player].choose_row(self.game_state.table, player)         # Определение номера забираемого ряда
                    self.inform_all("inform_row_chosen", player, row_index)
                    points = self.game_state.table.rows[row_index].truncate()                               # Подсчет штрафных очков в ряду и прибавление к счету игрока
                    player.score += points
                    print(f"{player.name}({player.score}): забирает ряд {row_index + 1}.\n"
                          f"\tКарта {card} становится 1-й в ряду {row_index + 1}")
                    self.game_state.table.rows[row_index].add_card(card)
                    player.hand.remove_card(card)
                    self.inform_all("inform_card_played", card)
            except ValueError as e:
                print(str(e))

        self.display_table_state()
        self.CHOSEN_CARD = {}
        return GamePhase.NEXT_PLAYER

    def next_player_phase(self) -> GamePhase:
        if self.turn_number <= self.INITIAL_HAND_SIZE:
            self.game_state.next_player()
            return GamePhase.CHOOSE_CARD
        else:
            return GamePhase.DECLARE_WINNER

    def declare_winner_phase(self) -> GamePhase:
        print('\nКонец игры. Результаты: ')
        for player in sorted(self.game_state.players, key = lambda x: (x.score)):
            name = player.name
            score = player.score
            print(name, score)

        print('Победитель:\n')
        min_score = min(player.score for player in self.game_state.players)
        winner = [player for player in self.game_state.players if player.score == min_score]
        print(winner)

        return GamePhase.GAME_END

def __main__():
    load_from_file = False
    if load_from_file:
        server = GameServer.load_game()
        server.save()
    else:
        server = GameServer.new_game(GameServer.get_player())
    server.run()


if __name__ == "__main__":
    __main__()