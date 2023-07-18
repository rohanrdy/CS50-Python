import pytest
from um import count

def test_all_cases_count():
    assert count("um, yeah you got that yummy yummy, yummy yummy, yuuummmmmmy yuummmy, UM lol") == 2