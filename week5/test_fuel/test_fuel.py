import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/3") == 33


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        assert convert("3/2")
