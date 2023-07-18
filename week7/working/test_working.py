import pytest
from working import convert

def test_validate_correct():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("9:00 PM to 5:30 AM") == "21:00 to 05:30"

def test_value_error_to():
    with pytest.raises(ValueError):
        assert convert("9:00 AM lol 5:30 PM")

def test_value_error_range():
    with pytest.raises(ValueError):
        assert convert("13:00 AM to 69:30 PM")