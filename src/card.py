class Card:

    NUMBERS = list(range(1,105))
    SCORE = [1, 2, 3, 5, 7]
    #COLORS = ['g', 'b', 'y', 'o', 'p']

    def  __init__(self, number: int, score: int):
        if number not in Card.NUMBERS:
            raise ValueError
        if score not in Card.SCORE:
            raise ValueError
        self.number = number
        self.score = score

    def __repr__(self):
        return f'{self.number}({self.score})'

    def save(self):
        return repr(self)

    def score(self, point):
        if self.number == 55:
            self.point += 7
        elif self.number % 11 == 0:
            self.point += 5
        elif self.number % 10 == 0:
            self.point += 3
        elif self.number % 5 == 0 and self.number % 10 != 0:
            self.point += 2
        else:
            self.point += 1
        return point