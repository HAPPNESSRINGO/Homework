#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Workshop 2

@author: Yiyang Wang 999028285
"""
#%% Exercise 1
# Point 1
# a. int   13

# b. float   5.5

# c. int   5

# d. int   1

# e. ZeroDivisionError

# f. ZeroDivisionError

# g. float   13.0

# h. str   hello

# i. str   hahaha

# j. int   11

# k. TypeError

# l. float   246.0

# m. int   246

# n. str   123123
# Point 2
# a
a = 11 + 2
print(a, type(a))

# b
b = 11 / 2
print(b, type(b))

# c
c = 11 // 2
print(c, type(c))

# d
d = 11 % 2
print(d, type(d))

# e
# e = 1 / 0
# ZeroDivisionError will be raised, so not executable

# f
# f = 1 % 0
# ZeroDivisionError will be raised, so not executable

# g
g = 11.0 + 2.0
print(g, type(g))

# h
h = 'he' + 'llo'
print(h, type(h))

# i
i = 'ha' * 3
print(i, type(i))

# j
j = len('hello') + 6
print(j, type(j))

# k
# k = 123 + '123'
# TypeError will be raised, so not executable

# l
l = 123 + 123.0
print(l, type(l))

# m
m = 123 + int('123')
print(m, type(m))

# n
n = str(123) + '123'
print(n, type(n))
# Point 3
# a's result is 13,g's result is 13.0.  a is int,but g is float.
# Point 4
#c is integer division,b is float division.% gets the remainder from integer division.
# Point 5
#e,f:The divisor can't be 0.  k:int can't plus string
# Point 6
# (l) integer (123) became a float (123.0),then they were added together.
# (m) string ('123') became a int (123),then they were added toghther.
# (n) int (123) became a str("123"),then print 123123
#%% Exercise 2
# Point 1
"""
a.
by hand:0
in console:4.440892098500626e-16

b.
by hand:0.00000001
in console:0.0

"""
# Point 2
"""
due to floating-point precision limits,
 where rounding errors and loss of significance affect numerical accuracy in programming.
"""
# Point 3
"""
No, none of the results are perfectly accurate.

we need for careful handling of floating-point operations in programming
"""

#%% Exercise 3
# Point 1
"""
round(0.5) :0
round(-1.5) : -2
round(2.5) : 2
round(3.5) : 4

"""
# Point 2
"""
The behavior observed here follows the round half to even strategy, 
also known as bankers’ rounding, 
which is the default behavior of the round() function in Python. 
"""
# Point 3
"""
a.X+1
b.Y-1
"""

#%% Exercise 4
# Point 1
float("123.45")
# Point 2
int(float('123.45'))
# Point 3
round(float('123.45') - int(float('123.45')),2)# use round(),turn 0.45000000000000284 into 0.45


#%% Exercise 5
# Point 1
name=input("What's your name?")
n=int(input("How many times do you want to repeat?"))
print(name*n)
# Point 2
name=input("What's your name?")
n=int(input("How many times do you want to repeat?"))
print((name+"\n")*n)

#%% Exercise 6
"""
f-string is useful
I learned to use it in 2017, in middle school.
(＾◡＾)/

"""
name=input("What is your name?")
age=int(input("How old are you?"))
print(f"Dear {name},you will turn 100 years old at {100-age+2024}")

#%% Exercise 7
# Prices of fruits
orange = 0.5
apple = 0.75
banana = 1.0

# User input for quantities
num_oranges = int(input("Enter the number of oranges you want to buy: "))
num_apples = int(input("Enter the number of apples you want to buy: "))
num_bananas = int(input("Enter the number of bananas you want to buy: "))

# Calculate total cost
total_cost = (num_oranges * orange) + (num_apples * apple) + (num_bananas * banana)

# Usd to rmb,then print total cost
# Assume the exchange rate is 7 RMB per 1 USD
print(f"Your total purchase is {total_cost*7} RMB")


#%% Exercise 8
# Point 1
# Input three names
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
name3 = input("Enter the third name: ")

# Rotate the variables
name1, name2, name3 = name2, name3, name1

# Print the results
print(f"After rotation: name1 = {name1}, name2 = {name2}, name3 = {name3}")
# Point 2
"""
Yes,it is.
Multi-variable assignment allows all expressions on the right side to be evaluated simultaneously 
and then assigned to the left-side variables.

"""


#%% Exercise 9
fahr=float(input("Fahrenheit:"))
cel=(fahr-32)/1.8
# use .2f 
print(f"{fahr:.2f} degrees Fahrenheit equals {cel:.2f} degrees Celsius.")

#%% Exercise 10
# period (0 for AM, 1 for PM)
hour = int(input("Enter the hour (1-12): "))
minute = int(input("Enter the minutes (0-59): "))
period = int(input("Enter the period (0 for AM, 1 for PM): "))

# Convert to 24-hour
hour = (hour % 12) + (period * 12)

# Print the result
print(f"{hour}:{minute:02d}")