import pytest

from src.card import Card

def test_init():
    c = Card(55,7)
    assert c.number == 55
    assert c.score == 7

def test_save():
    c = Card(55,7)
    assert repr(c) == '55(7)'
    assert c.save() == '55(7)'

def test_score():
    c = Card(55, 7)