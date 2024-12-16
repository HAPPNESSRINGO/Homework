from lab9_ex2_template import sum_of_integers, count_vowels, compress, int_from_list, hyperfactorial, hyper_list, equal_odds

#######################################
# Testing of sum_of_integers function #
#######################################
def test_sum_of_integers():
    assert sum_of_integers(5) == 15, "sum_of_integers(5) expected 15"
    assert sum_of_integers(1) == 1, "sum_of_integers(1) expected 1"
    assert sum_of_integers(0) == 0, "sum_of_integers(0) expected 0"
    assert sum_of_integers(10) == 55, "sum_of_integers(10) expected 55"


####################################
# Testing of count_vowels function #
####################################
def test_count_vowels():
    assert count_vowels("") == 0, 'count_vowels("") expected 0'
    assert count_vowels("every night i dream about python") == 10, \
        'count_vowels("every night i dream about python") expected 10'
    assert count_vowels("onomatopoeia") == 8, \
        'count_vowels("onomatopoeia") expected 8'
    assert count_vowels("bcdfg") == 0, 'count_vowels("bcdfg") expected 0'


################################
# Testing of compress function #
################################
def test_compress():
    assert compress([1, 2, 3, 4, 5, 6]) == [7, 7, 7], \
        "compress([1,2,3,4,5,6]) expected [7,7,7]"
    assert compress([1, 2, 3, 4, 5, 6, 7]) == [8, 8, 8, 4], \
        "compress([1,2,3,4,5,6,7]) expected [8,8,8,4]"
    assert compress([4, 2]) == [6], "compress([4,2]) expected [6]"
    assert compress([3]) == [3], "compress([3]) expected [3]"
    assert compress([]) == [], "compress([]) expected []"

#####################################
# Testing of int_from_list function #
#####################################
def test_int_from_list():
    assert int_from_list([1, 2, 0, 0, 8]) == 12008, "int_from_list([1,2,0,0,8]) expected 12008"
    assert int_from_list([3, 8, 8]) == 388, "int_from_list([3,8,8]) expected 388"
    assert int_from_list([1]) == 1, "int_from_list([1]) expected 1"
    assert int_from_list([]) == 0, "int_from_list([]) expected 0"



######################################
# Testing of hyperfactorial function #
######################################
def test_hyperfactorial():
    assert hyperfactorial(1) == 1, "hyperfactorial(1) expected 1"
    assert hyperfactorial(2) == 4, "hyperfactorial(2) expected 4"
    assert hyperfactorial(3) == 108, "hyperfactorial(3) expected 108"

##################################
# Testing of hyper_list function #
##################################
def test_hyper_list():
    assert hyper_list(5) == [1, 4, 108, 27648, 86400000], \
        "hyper_list(5) expected [1,4,108,27648,86400000]"
    assert hyper_list(0) == [], "hyper_list(0) expected []"
    assert hyper_list(1) == [1], "hyper_list(1) expected [1]"

##################################
# Testing of equal_odds function #
##################################
def test_equal_odds():
    assert equal_odds(11111, 5) is True, "equal_odds(11111,5) expected True"
    assert equal_odds(111111, 5) is False, "equal_odds(111111,5) expected False"
    assert equal_odds(12345, 333) is True, "equal_odds(12345,333) expected True"
    assert equal_odds(907, 29305) is False, "equal_odds(907,29305) expected False"
    assert equal_odds(0, 0) is True, "equal_odds(0,0) expected True"
    assert equal_odds(284, 606) is True, "equal_odds(284,606) expected True"
