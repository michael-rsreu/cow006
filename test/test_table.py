import json
from src.card import Card
from src.row import Row
from src.table import Table

def test_init():
    table = Table()
    assert len(table.rows) == 4
    assert (isinstance(row, Row) for row in table.rows)         # Является ли row объектом класса Row

def test_repr():
    table = Table()

    table.rows[0].add_card(Card(10))
    table.rows[1].add_card(Card(25))
    table.rows[2].add_card(Card(50))
    table.rows[3].add_card(Card(60))
    table.rows[2].add_card(Card(55))
    table.rows[3].add_card(Card(62))
    table.rows[3].add_card(Card(67))

    expected_repr = f"row1: 10(3)\nrow2: 25(2)\nrow3: 50(3) 55(7)\nrow4: 60(3) 62(1) 67(1)"
    assert repr(table) == expected_repr

def test_add_card():
    table = Table()

    table.rows[0].add_card(Card(7))
    table.rows[1].add_card(Card(85))
    table.rows[2].add_card(Card(69))
    table.rows[3].add_card(Card(55))

    table.add_card(Card(9))
    table.add_card(Card(86))
    table.add_card(Card(75))
    table.add_card(Card(60))

    assert repr(table[0]) == '7(1) 9(1)'
    assert repr(table[1]) == '85(2) 86(1)'
    assert repr(table[2]) == '69(1) 75(2)'
    assert repr(table[3]) == '55(7) 60(3)'
    assert not table.add_card(Card(5))
    assert not table.add_card(Card(1))

def test_save():
    table = Table()

    table.rows[0].add_card(Card(7))
    table.rows[1].add_card(Card(85))
    table.rows[2].add_card(Card(69))
    table.rows[3].add_card(Card(55))

    table.add_card(Card(9))
    table.add_card(Card(86))
    table.add_card(Card(75))
    table.add_card(Card(60))

    save_data = table.save()
    json_data = json.dumps({
        'row1': '7 9',
        'row2': '85 86',
        'row3': '69 75',
        'row4': '55 60'
    }, sort_keys=True)

    assert save_data == json_data

def test_load():
    data = {
        'row1': '7 9',
        'row2': '85 86',
        'row3': '69 75',
        'row4': '55 60'
    }

    table = Table.load(data)
    assert table[0].cards[1] == Card(9)
    assert table[3].cards[0] == Card(55)
    assert len(table[1].cards) == 2
    assert len(table[2].cards) == 2