import pytest
from numb3rs import validate


def test_validate_correct():
    assert validate("69.42.50.255") == True
    assert validate("17.0.0.1") == True


def test_validate_wrong():
    assert validate("rohan") == False
    assert validate("420.1337.8055.13") == False


def test_validate_less_periods():
    assert validate("0") == False
    assert validate("69.420") == False


def test_validate_first_byte():
    assert validate("300.69.69.69") == False
    assert validate("1.420.69.0") == False