from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HELLO THERE") == 0

def test_h():
    assert value("hehehe") == 20
    assert value("Hahaha") == 20

def test_others():
    assert value("Rohan") == 100