from src.hand import Hand
from src.player import Player


def test_init():
    h = Hand.load("55 103 44")
    p = Player(name="Alex", hand=h, score=15)
    assert p.name == "Alex"
    assert p.hand == h
    assert p.score == 15


def test_str():
    h = Hand.load("55 103 44")
    p = Player(name="Alex", hand=h, score=15)
    assert str(p) == "Alex(15): 55 103 44"    # В строке рядом с номиналом карт в скобках их очки должны писаться. Как это сделать?


def test_save():
    h = Hand.load("55 103 44")
    p = Player(name="Alex", hand=h, score=15)
    assert p.save() == {"name": "Alex", "score": 15, "hand": "55 103 44"}


def test_eq():
    h1 = Hand.load("55 103 44")
    h2 = Hand.load("55 103 44")
    p1 = Player(name="Alex", hand=h1, score=15)
    p2 = Player(name="Alex", hand=h2, score=15)
    assert p1 == p2


def test_load():
    data = {"name": "Alex", "score": 15, "hand": "55 103 44"}
    h = Hand.load("55 103 44")
    p_expected = Player(name="Alex", hand=h, score=15)
    p = Player.load(data)
    assert p == p_expected