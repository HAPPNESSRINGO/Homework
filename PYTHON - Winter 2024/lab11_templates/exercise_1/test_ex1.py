from ex1 import is_sorted

def test_already_sorted():
    assert is_sorted([1, 2, 3, 4, 5]) == True

def test_reverse_sorted():
    assert is_sorted([5, 4, 3, 2, 1]) == False

def test_unsorted():
    assert is_sorted([3, 1, 4, 2, 5]) == False

def test_single_element():
    assert is_sorted([1]) == True

def test_empty_list():
    assert is_sorted([]) == True

def test_duplicates_sorted():
    assert is_sorted([1, 2, 2, 3, 4]) == True

def test_duplicates_unsorted():
    assert is_sorted([1, 3, 2, 2, 4]) == False

def test_all_same_elements():
    assert is_sorted([2, 2, 2, 2, 2]) == True

def test_negative_numbers_sorted():
    assert is_sorted([-5, -4, -3, -2, -1]) == True

def test_negative_numbers_unsorted():
    assert is_sorted([-1, -3, -2, -5, -4]) == False

def test_mixed_numbers_sorted():
    assert is_sorted([-3, -1, 0, 2, 4]) == True
    