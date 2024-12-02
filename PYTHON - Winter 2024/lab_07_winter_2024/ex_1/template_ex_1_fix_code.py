#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python TC 7 

@author: Yiyang Wang 999028285
python-winter-2024
Exercise 1 
 

Let's fix the code! 

In each item fix the code and add an explanation in English using your own voice, remember to use technical programming vocabulary for the justifications. You can use the Glossary1 of the course if you need help with your vocabulary. Beware that using the words from any LLM (like ChatGPT, Doubao, Baidu chatbot, etc.) is not using your own voice to answer. 
"""


# %% Problem A:
# Description: A function is defined to add two numbers and return the result, but the code contains errors.
# Code with Errors:

def add_numbers(a, b):#miss :
    return a + b #it should be "return"


result = add_numbers (1, 2) #miss ()
print(result)


# %% Problem B:
# We want the function to return the squared value of the number given as parameter to the function. 
# Code with Error:

def square_number(n):#miss n
    squared = n * n
    return squared # return the squared


result = square_number(4)
print(result)


# %% Problem C:
# We want the function that modifies a list, doubles all the numbers in a list received as parameter. 
# Code with Error:

def double(a_list):# miss argument
    """ 
    This function assumes all items in the list are numbers.  
    Modifies the argument: double all the items. 
    """

    for index in range(len(a_list)):
        a_list[index] = a_list[index]*2


my_list = [1, 5, 3, 8, 7]
double(my_list)# pass the argument
print(my_list)


# %% Problem D:
# We want the function that modifies a list, incrementing all the numbers in a list received as parameter. 
# Code with Error:

def increment_list(a_list):
    """ 
    This function assumes all items in the list are numbers.  
    Modifies the argument: incrementing all the items by 1. 
    """
    for position in range(len(a_list)):
        a_list[position] += 1


numbers = [1, 3, 5, 7, 9]  # this should not be modified
new_numbers = numbers[:]  # Create a copy of the list
increment_list(new_numbers)

print(f"The original numbers are {numbers}, the incremented copy of numbers is {new_numbers}")


# %% Problem E:
# We want the function that modifies a list, removing all the letters "the_letter" received as parameter. 
# Change only one line in the function to fix this.
# Code with Error:


def remove_from_list(the_letter, letters):
    """ 
    This function modifies the letters, removing all the_letter from it. 
    """
    for position in range(-1, -len(letters)-1, -1):#from the last letter to the first letter
        element = letters[position]
        if element == the_letter:
            letters.pop(position)


my_letters = ["a", "b", "b", "c", "b"]
remove_from_list("b", my_letters)
print(my_letters)
