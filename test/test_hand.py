from src.card import Card
from src.hand import Hand

cards = [Card(8), Card(13), Card(55), Card(44), Card(3)]

def test_init():
    d = Hand(cards=cards)
    assert d.cards == cards

def test_repr():
    d = Hand(cards)
    d1 = Hand([Card(10)])

    assert d.__repr__() == "8 13 55 44 3"
    assert d1.__repr__() == "10"
    assert Hand([Card(3)]).__repr__() == "3"

def test_eq():
    h = Hand(cards)
    h1 = Hand(cards)
    h2 = Hand([Card(30), Card(55), Card(44)])
    h3 = Hand([Card(103)])

    assert h == h1
    assert h2 != h3
    assert h != h2

def test_score():
    h = Hand.load('8 13 55 44 3')
    assert h.score() == 1 + 1 + 7 + 5 + 1

    h1 = Hand.load('44 104 55 33')
    assert h1.score() == 5 + 1 + 7 + 5

def test_add_card():
    h = Hand.load('8 13 55')
    h.add_card(Card.load('5'))
    assert h == '8 13 55 5'

    h = Hand.load('44 104 55')
    h.add_card(Card.load('1'))
    assert h == '44 104 55 1'

def test_remove_card():
    h = Hand.load('8 13 55')
    h.remove_card(Card.load('13'))
    assert h == '8 55'

    h = Hand.load('44 104 55 1')
    h.remove_card(Card.load('1'))
    assert h == '44 104 55'

def test_save():
    h = Hand(cards=cards)
    assert h.save() == "8 13 55 44 3"

    h = Hand(cards=[Card(55), Card(12)])
    assert h.save() == "55 12"

def test_load():
    h = Hand(cards=cards)
    h1 = Hand.load("8 13 55 44 3")
    assert h == h1