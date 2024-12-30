from ex5 import get_missing_characters


def test_all_letters():
    sentence = "abcdefghijklmnopqrstuvwxyz"
    assert get_missing_characters(sentence) == []

def test_empty():
    sentence = ""
    assert get_missing_characters(sentence) == list("abcdefghijklmnopqrstuvwxyz")

def test_single_letter():
    sentence = "a"
    assert get_missing_characters(sentence) == list("bcdefghijklmnopqrstuvwxyz")
    
def test_all_letters_sentence():
    sentence = "the quick brown fox jumps over the lazy dog"
    assert get_missing_characters(sentence) == []

def test_non_alpha_characters():
    sentence = "1234567890!@#$%^&*()_+-=[]{}|;':,.<>/?"
    assert get_missing_characters(sentence) == list("abcdefghijklmnopqrstuvwxyz")

def test_repeated_letters():
    sentence = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssss"
    assert get_missing_characters(sentence) == list("tuvwxyz")
