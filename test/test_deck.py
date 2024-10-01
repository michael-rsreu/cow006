from src.deck import Deck
from src.card import Card

import random

cards = [Card(8), Card(13), Card(55), Card(44), Card(3)]

def test_init():
    d = Deck(cards=cards)
    assert d.cards == cards

def test_repr():
    d = Deck(cards)
    d1 = Deck([Card(10)])

    assert d.__repr__() == "8(1) 13(1) 55(7) 44(5) 3(1)"
    assert d1.__repr__() == "10(3)"

def test_save():
    d = Deck(cards = cards)
    assert d.save() == '8(1) 13(1) 55(7) 44(5) 3(1)'

    d = Deck(cards = [Card(10), Card(55), Card(12)])
    assert d.save() == '10(3) 55(7) 12(1)'

def test_load():
    d = Deck.load('8 13 55 44 3')
    expected_deck = Deck(cards)
    assert d == expected_deck

def test_shuffle_1():
    """Проверяет, изменился ли порядок карт в колоде"""
    deck1 = Deck(None)
    deck2 = Deck(None)
    assert len(deck1.cards) == len(deck2.cards)
    assert deck1.cards != deck2.cards

def test_shuffle_2():
    """Проверяет перемешанную колоду на несоответствие исходной"""
    random.seed(3)

    cards = Card.all_cards()
    deck = Deck(cards=cards)
    deck1 = deck.save()

    deck.shuffle()
    assert deck.save() != deck1

    deck.shuffle()
    assert deck.save() != deck1

    deck.shuffle()
    assert deck.save() != deck1

def test_draw_card():  # ne rabotaet
    d = Deck.load([10, 12, 55])
    assert d.draw_card() == Card.load('10(3)')
    assert d == '12(1) 55(7)'