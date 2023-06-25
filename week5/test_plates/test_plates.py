from plates import is_valid

def test_normal():
    assert is_valid("IN1947") == True
    assert is_valid("mbappe") == True

def test_length():
    assert is_valid("NeverGonnaGiveYouUp") == False
    assert is_valid("x") == False

def test_num_in_middle():
    assert is_valid("ab69cd") == False
    assert is_valid("cs50p") == False

def test_first_num_zero():
    assert is_valid("ab0123") == False
    assert is_valid("xy420z") == False

def test_no_punctuation():
    assert is_valid("xx,.&!") == False
    assert is_valid("xx <42>") == False

def test_first_two_alpha():
    assert is_valid("07bond") == False
    assert is_valid("r0han") == False
    assert is_valid("rr") == True
    assert is_valid("8055") == False

def test_Captital():
    assert is_valid("IAMGROOT") == False
    assert is_valid("CS1337") == True