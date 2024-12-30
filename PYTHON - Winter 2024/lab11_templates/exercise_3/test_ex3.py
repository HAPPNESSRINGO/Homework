from ex3 import sort_2, sort_3

#####################
# Testing of sort_2 #
#####################
def test_sort_2_sorted():
    assert sort_2([1, 2]) == [1, 2]

def test_sort_2_unsorted():
    assert sort_2([2, 1]) == [1, 2]

def test_sort_2_equal():
    assert sort_2([1, 1]) == [1, 1]
    
def test_sort_2_negative():
    assert sort_2([1, -1]) == [-1, 1]

#####################
# Testing of sort_3 #
#####################
def test_sort_3_sorted():
    assert sort_3([1, 2, 3]) == [1, 2, 3]

def test_sort_3_unsorted():
    assert sort_3([3, 1, 2]) == [1, 2, 3]

def test_sort_3_reverse():
    assert sort_3([3, 2, 1]) == [1, 2, 3]

def test_sort_3_equal2():
    assert sort_3([2, 1, 2]) == [1, 2, 2]
    
def test_sort_3_equal3():
    assert sort_3([2, 2, 2]) == [2, 2, 2]
