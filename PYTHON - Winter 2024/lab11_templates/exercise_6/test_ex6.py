from ex6 import sliding_window_median


def test_single_element_window_sorted():
    nums = [1, 2, 3, 4, 5]
    k = 1
    assert sliding_window_median(nums, k) == [1, 2, 3, 4, 5]
    
def test_window_reverse_sorted():
    nums = [5, 4, 3, 2, 1]
    k = 1
    assert sliding_window_median(nums, k) == [5, 4, 3, 2, 1]
    
def test_window_mixed():
    nums = [6, 2, 4, 3, 5, 1]
    k = 4
    assert sliding_window_median(nums, k) == [3, 3, 3]

def test_window_size_equals_list_length():
    nums = [1, 2, 3, 4, 5]
    k = len(nums)
    assert sliding_window_median(nums, k) == [3]

def test_window_size_greater_than_list_length():
    nums = [1, 2, 3, 4, 5]
    k = 6
    assert sliding_window_median(nums, k) == []

def test_empty_list1():
    nums = []
    k = 1
    assert sliding_window_median(nums, k) == []
    
def test_empty_list2():
    nums = []
    k = 3
    assert sliding_window_median(nums, k) == []

def test_all_elements_equal():
    nums = [2, 2, 2, 2, 2]
    k = 3
    assert sliding_window_median(nums, k) == [2, 2, 2]

def test_negative_numbers():
    nums = [-1, -2, -3, -4, -5]
    k = 3
    assert sliding_window_median(nums, k) == [-2, -3, -4]

def test_large_window_sorted():
    nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    k = 4
    assert sliding_window_median(nums, k) == [3, 5, 7, 9, 11, 13, 15]

def test_large_window_mixed():
    nums = [5, 9, 3, 7, 14, 10, 15, 1, 20, 17]
    k = 4
    assert sliding_window_median(nums, k) == [5, 7, 7, 10, 10, 10, 15]
     