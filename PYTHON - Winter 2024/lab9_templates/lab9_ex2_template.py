##############
# Exercise 2 #
##############

#%% Problem A: Sum of Integers
# Description: Function that returns the sum of integers 1 to n
def sum_of_integers(n: int) -> int:
    # Base case
    if n <= 0:
        return 0
    # Recursive case
    return n + sum_of_integers(n - 1)


#%% Problem B: Count Vowels
# Description: Function that returns the number of vowels in a string
def count_vowels(a_string: str) -> int:
    vowels = 'ieaou'
    # Base case
    if a_string == '':
        return 0
    # Recursive case
    first_char = a_string[0]
    count = 1 if first_char in vowels else 0
    return count + count_vowels(a_string[1:])


#%% Problem C: Compress List
# Description: Function that compresses a list by summing the first and last elements
def compress(a_list:list[int]) -> list[int]:
    # Base case
    if len(a_list) == 0:
        return []
    if len(a_list) == 1:
        return [a_list[0]]
    # Recursive case: sum first and last, then recurse on the middle part
    return [a_list[0] + a_list[-1]] + compress(a_list[1:-1])


#%% Problem D: Integer from List
# Description: Function that returns an integer whose digits defined in a list
def int_from_list(a_list:list[int]) -> int:
    # Base case
    if len(a_list) == 0:
        return 0
    # Recursive case
    # If we consider the first digit times 10^(len-1)
    # or we can build from the left:
    return a_list[0] * (10 ** (len(a_list) - 1)) + int_from_list(a_list[1:])


#%% Problem E1: Hyperfactorial
# Description: Function that returns the hyperfactorial of a positive integer
def hyperfactorial(n:int) -> int:
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    return hyperfactorial(n - 1) * (n ** n)

# Problem E2: Hyperfactorial List
# Description: Function that returns a list of hyperfactorials up to n
def hyper_list(n:int) -> list:
    # Base case
    if n == 0:
        return []
    # Recursive case
    return hyper_list(n - 1) + [hyperfactorial(n)]


#%% Problem F: Equal Odds
# Description: Function that returns true if two positive integers have the same sum of odd digits
def equal_odds(n1:int, n2:int)->bool:
    # Base case
    if n1 == 0 and n2 == 0:
        return True  # when both are zero, their odd sums are both zero
    # Extract last digits
    d1 = n1 % 10
    d2 = n2 % 10
    # Determine odd sum contribution for this recursion step
    odd_contrib_1 = d1 if d1 % 2 == 1 else 0
    odd_contrib_2 = d2 if d2 % 2 == 1 else 0

    def sum_odd_digits(x: int) -> int:
        if x == 0:
            return 0
        return ((x % 10) if (x % 10) % 2 == 1 else 0) + sum_odd_digits(x // 10)

    return sum_odd_digits(n1) == sum_odd_digits(n2)
