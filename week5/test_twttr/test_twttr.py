from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("rohan") == "rhn"
    assert shorten("ROHan") == "RHn"
    assert shorten("12345Abcde") == "12345bcd"
    assert shorten(",REDDY.") == ",RDDY."