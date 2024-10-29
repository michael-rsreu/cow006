from src.card import Card
from src.row import Row

cards = [Card(8), Card(13), Card(55), Card(44), Card(3)]

def test_init():
    r = Row()
    assert r.__init__() == None

def test_repr():
    r = Row()
    assert r.__repr__() == ''

    r.add_card(Card.load('13'))
    assert r.__repr__() == '13'

def test_add_card():
    r = Row()
    r.add_card(Card(5))
    r.add_card(Card(55))
    assert r.cards == [Card(5), Card(55)]
    assert r.cards != [Card(55)]

def test_max_lengh():
    r = Row()
    r.add_card(Card(5))
    assert not r.has_max_lengh()

    r.add_card(Card(11))
    r.add_card(Card(13))
    r.add_card(Card(103))
    r.add_card(Card(100))
    r.add_card(Card(3))
    assert r.has_max_lengh()

def test_truncate():
    r = Row()
    r.add_card(Card(1))
    r.truncate()
    assert r.cards == []

def test_can_play_on():
    r = Row()
    assert r.can_play_on(Card(20))

    r.add_card(Card(21))
    assert not r.can_play_on(Card(20))
    assert r.can_play_on(Card(22))