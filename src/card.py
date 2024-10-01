class Card:
    NUMBERS = list(range(1,105))
    #SCORE = [1, 2, 3, 5, 7]
    #COLORS = ['g', 'b', 'y', 'o', 'p']

    def __init__(self, number: int):
        if number not in Card.NUMBERS:
            raise ValueError
        self.number = number

    def __repr__(self):
        return f'{self.number}({self.score()})'

    def __eq__(self, other):    #а надо ли eq, если такое же сравнение есть в can_play_on
        return self.number == other.number

    def save(self):
        return repr(self)

    def score(self):
        if self.number == 55:
            return 7
        elif self.number % 11 == 0:
            return 5
        elif self.number % 10 == 0:
            return 3
        elif self.number % 5 == 0 and self.number % 10 != 0:
            return 2
        else:
            return 1

    def can_play_on(self, other):
        return self.number > other.number

    def load(text: str):
        #По идее нам не надо вводить штрафные очки каждой карты, т.к. они определяются в Score
        return Card(number=int(text))

    def all_cards(numbers: None | list[int] = None):     # Нужна ли она вообще
        if numbers is None:
            numbers = Card.NUMBERS
        cards = [Card(number=num) for num in numbers]
        return cards