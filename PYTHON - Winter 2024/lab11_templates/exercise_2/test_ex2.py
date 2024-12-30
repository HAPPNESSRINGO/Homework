from ex2 import sorted_by_map, sort_by_map

############################
# Testing of sorted_by_map #
############################
def test_sorted_by_map():
    assert sorted_by_map(list('abcdefghij'), [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == list('jihgfedcba')

def test_sorted_by_map_empty():
    assert sorted_by_map([], []) == []

def test_sorted_by_map_single_element():
    assert sorted_by_map(['a'], [0]) == ['a']

def test_sorted_by_map_reverse_order():
    assert sorted_by_map(['a', 'b', 'c'], [2, 1, 0]) == ['c', 'b', 'a']

def test_sorted_by_map_duplicate_elements():
    assert sorted_by_map(['a', 'b', 'a'], [1, 2, 0]) == ['a', 'a', 'b']

def test_sorted_by_map_random_order():
    assert sorted_by_map(['a', 'b', 'c', 'd'], [3, 0, 2, 1]) == ['b', 'd', 'c', 'a']
    
def test_sorted_by_map_maintain_order():
    assert sorted_by_map(['a', 'b', 'c', 'd'], [0, 1, 2, 3]) == ['a', 'b', 'c', 'd']

##########################
# Testing of sort_by_map #
##########################
def test_sort_by_map():
    a_list = list('abcdefghij')
    sort_by_map(a_list, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    assert a_list == list('jihgfedcba')
    
def test_sort_by_map_empty():
    a_list = []
    sort_by_map(a_list, [])
    assert a_list == []

def test_sort_by_map_single_element():
    a_list = ['a']
    sort_by_map(a_list, [0])
    assert a_list == ['a']

def test_sort_by_map_reverse_order():
    a_list = ['a', 'b', 'c']
    sort_by_map(a_list, [2, 1, 0])
    assert a_list == ['c', 'b', 'a']

def test_sort_by_map_duplicate_elements():
    a_list = ['a', 'b', 'a']
    sort_by_map(a_list, [1, 2, 0])
    assert a_list == ['a', 'a', 'b']

def test_sort_by_map_all_same_elements():
    a_list = ['a', 'a', 'a']
    sort_by_map(a_list, [2, 1, 0])
    assert a_list == ['a', 'a', 'a']

def test_sort_by_map_random_order():
    a_list = ['a', 'b', 'c', 'd']
    sort_by_map(a_list, [3, 0, 2, 1])
    assert a_list == ['b', 'd', 'c', 'a']
