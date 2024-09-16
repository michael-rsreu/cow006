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
        return f'{self.number}{self.score}'