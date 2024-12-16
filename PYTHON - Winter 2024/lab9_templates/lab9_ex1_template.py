################
## Exercise 1 ##
# Fix the Code #
################
from homework_winter2024.template_workshop_3 import result


#%% Problem A
# Description: Function that prints a count down from n to 1
def countdown(n:int) -> None:
    if n == 0:
        print('Ready!')
    else:
        print(f'Counting down: {n}')
        countdown(n - 1) #It should decrease by 1.
    
countdown(5)
"""
Counting down: 5
Counting down: 4
Counting down: 3
Counting down: 2
Counting down: 1
Ready!
"""
    
#%% Problem B
# Description: Function that prints all elements of a list
def print_elements(a_list:list[int]) -> None:
    if len(a_list) != 0:
        print(a_list[0], end=' ')
        print_elements(a_list[1:]) # Remove the first elements.

print_elements([1,2,3,4,5])
"""
1 2 3 4 5
"""

#%% Problem C
# Description: Function that prints all characters in even positions of a string
def print_chars(a_string:str) -> None:
    if len(a_string) != 0:
        print(a_string[0], end=' ')
        print_chars(a_string[2:]) # Skip the even position.

print_chars('ABCDEFGH')
"""
A C E G
"""

#%% Problem D
# Description: Function that prints the odd numbers from 1 to n
def print_all_odds(n:int) -> None:
    if n != 0:
        print_all_odds(n - 1) # Decrease n in each recursive call.
        if n % 2:
            print(n, end=' ')
    
print_all_odds(20)
"""
1 3 5 7 9 11 13 15 17 19
"""

#%% Problem E
# Description: Function that returns the sum of a list of integers
def sum_of_list(a_list:list[int]) -> int:
    if len(a_list) == 0:
        result = 0  # Return 0 for an empty list.
    else:
        result = a_list[0] + sum_of_list(a_list[1:])
    return result

print(sum_of_list([1,2,3,4,5]) == 15) # should print True

#%% Problem F
# Description: Function that triples each element of a list
def triple_elements(a_list:list[int]) -> list[int]:
    if len(a_list) == 0:
        result = [] # It should return an empty list
    else:
        result = [3*a_list[0]] + triple_elements(a_list[1:])
    return result

print(triple_elements([1,2,3,4,5]) == [3, 6, 9, 12, 15]) # should print True

#%% Problem G
# Description: Function that returns a matrix (list of lists) of zeros of size (rows x cols)
def zeros(rows, cols) -> list[list[int]]:
    if rows == 0:
        result = [] # It should return an empty list
    else:
        result = [[0] * cols] + zeros(rows - 1, cols)  #  Append a new row of zeros
    return result

print(zeros(3, 4) == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) # should print True

#%% Problem Z
# Description: Function that returns a string with alternating upper and lower case characters
def alternate_case(string:str) -> str:
    if len(string) == 0:
        result = ''
    elif len(string) == 1:
        result = string[0].upper()
    else:
        result = string[0].upper() + string[1].lower() + alternate_case(string[2:]) # # Ensures alternate case by processing two characters at a time, starting from the third character for recursion.
    return result

print(alternate_case('zzzzzzzz') == 'ZzZzZzZz') # should print True
