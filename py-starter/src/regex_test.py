from src.regex import remove_digits


def test_remove_digits():
    assert remove_digits("arthur 42") == "arthur "
