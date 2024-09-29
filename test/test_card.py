from src.card import Card

def test_init():
    c = Card(55)
    assert c.number == 55
    assert c.score() == 7

def test_save():    # Не фурычит(
    c = Card(55)
    assert repr(c) == '55(7)'
    assert c.save() == '55(7)'

    c = Card(13)
    assert repr(c) == '13(1)'
    assert c.save() == '13(1)'

def test_score():
    c = Card(55)
    assert c.score() == 7
    c = Card(13)
    assert c.score() == 1
    c = Card(44)
    assert c.score() == 5

def test_can_play_on():
    c1 = Card(77)
    c2 = Card(13)
    c3 = Card(55)

    assert c1.can_play_on(c1) == False
    assert c1.can_play_on(c2) == True
    assert c2.can_play_on(c3) == False

def test_load():
    a = '77'
    c = Card.load(a)
    assert c == Card(77)

    b = '13'
    c = Card.load(b)
    assert c == Card(13)