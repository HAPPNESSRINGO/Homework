# -*- coding: utf-8 -*-
"""
Python Workshop 3 - Homework 2

@author: Yiyang Wang 999028285 
"""
#%% Exercise 1
# Complete each comment below the statements. 
# Replace the ... with your answer.

result_a = "C" == 'C' 
# result_a is True because The expression checks if the string "C" is equal to the character 'C', and since they are the same, the result is True.
result_b = "F" or "K" 
# result_b is "F" because In Python, the or operator returns the first truthy value. Since "F" is a non-empty string (which is truthy), it is returned. 
result_c = "F" and "K" 
# result_c is "K" because The and operator returns the last evaluated argument if all are truthy. Both "F" and "K" are non-empty strings (truthy), so "K" is returned.
result_d = len("gtiit") >= len("GTIIT") 
# result_d is True because The length of both strings is 5, so the condition 5 >= 5 evaluates to True.
result_e = 'a' != 'A'
# result_e is True because In ASCII, lowercase letters have higher values than uppercase ones. 'a' (ASCII value 97) is greater than 'A' (ASCII value 65).
result_f = 'A' < 'Z' 
# result_f is True because In ASCII, 'A' (value 65) comes before 'Z' (value 90), so 'A' < 'Z' is True.
result_g = "GTIIT" == "gtiit"
# result_g is False because String comparison is case-sensitive, so "GTIIIT" and "gtiit" are not the same.
result_h = 0 and "GT" 
# result_h is  0 because The and operator stops at the first falsy value, which is 0, so it returns 0.
result_i = "GT" and 0 
# result_i is 0 because Both "GT" (truthy) and 0 (falsy) are evaluated, but the and operator returns the last value if the first is truthy, so 0 is returned. 
result_j = (6==7) and a_variable 
# result_j is False because The condition 6==7 is False, and the and operator short-circuits here, so a_variable is never evaluated. The result is False, and there is no error despite a_variable being undefined.
# Why does this work although a_variable doens't exist?
result_k = 0 or "" 
# result_k is ""  because The or operator returns the first truthy value. Here, both 0 and "" are falsy, so the last value, "", is returned.
result_l = "GTIIT" or 1/0 
# result_l is "GTIIIT" because The or operator short-circuits at the first truthy value, so "GTIIIT" is returned, and 1/0 (which would raise a ZeroDivisionError) is not evaluated.
# Why does this work although 1/0 gives ZeroDivisionError?
result_m = 0.00000001 + 1000000000 - 1000000000 > 0.0
# result_m is False because due to floating-point precision, the result might not be exactly 0.00000001. Instead, it is rounded down to 0.0, which makes the comparison 0.0 > 0.0 evaluate to False.
result_n = (2**0.5)**2 == 2
# result_n is False because due to the limited precision of floating-point arithmetic

#%% Exercise 2
# Get temperature 
temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C, F, K): ").upper()

# Check 
if unit == 'C':
    # In Celsius, no conversion needed
    result = temp
    print(f"The temperature in Celsius is: {result:.2f}°C")
elif unit == 'F':
    # Fahrenheit to Celsius
    result = (temp - 32) * 5/9
    print(f"The temperature in Celsius is: {result:.2f}°C")
elif unit == 'K':
    # Kelvin to Celsius
    result = temp - 273.15
    print(f"The temperature in Celsius is: {result:.2f}°C")
else:
    # Handle invalid units
    print("Error: Invalid unit entered.")

#%% Exercise 3
# Get input from the user
students = int(input("Enter the number of students: "))
sodas = int(input("Enter the number of sodas: "))
pizzas = int(input("Enter the number of pizzas: "))
is_weekend = input("Is it the weekend? (Yes/No): ").strip().lower() == 'yes'

# Determine if the party is successful based on the criteria
is_successful = (
    (sodas >= 2 * pizzas and pizzas >= students / 2) if not is_weekend else
    (pizzas >= students and sodas > 2 * students)
)

# Print the result
print("Is the party successful? ", "Yes" if is_successful else "No")

#%% Exercise 4
# Get two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Determine the shorter and longer strings
short = string1 if len(string1) <= len(string2) else string2
long = string1 if len(string1) > len(string2) else string2

# Print the output
output = short + long + short
print("Output string:", output)

#%% Exercise 5
# Ask the user for an integer number
num = int(input("Enter an integer: "))

# Initialize the result as an empty string
result = ""

# Check divisibility by 3, 5, and 7 and append to result
result += "Fizz" if num % 3 == 0 else ""
result += "Buzz" if num % 5 == 0 else ""
result += "Daah" if num % 7 == 0 else ""

# Print the result or the number itself if not divisible by 3, 5, or 7
print(result if result else num)

#%% Exercise 6

# Fix the semantic errors in this code. 
# You need to fix 6 lines of code in total to make it work. 
# You don't have to write all the code again. 
# Just fix either a variable, operators, or indentation of code.
# Add a comment at each line explaining the fix.
"""
Examines three variables (x, y and z) and prints the largest, odd number among them.
If none of them are odd, it should print a message reflecting that situation.
""" 

x = int(input("Enter the first number (x): "))# should ensure x is an integer type
y = int(input("Enter the second number (y): ")) 
z = int(input("Enter the third number (z): ")) 
 
# Initialize largest_odd to: 0 if no odd number,  
# or to: the value of the first odd in the options 
largest_odd = max(x if x % 2 != 0 else 0, y if y % 2 != 0 else 0, z if z % 2 != 0 else 0) # may not initialize largest_odd properly if only one or two numbers are odd. 


# Check each number and update largest_odd if it is odd and greater than current largest_odd 
if largest_odd == 0: # fixed，because of (if),we should use =.
    # This text is printed when all are even
    print("None of them are odd") 
else: 

    if y % 2 != 0 and (y > largest_odd): 
        largest_odd = y # it should be y. 
    if z % 2 != 0 and (z > largest_odd): # fixed，it incorrectly uses logical operations for initialization, leading to faulty short-circuit behavior and incorrect results.
        largest_odd = z # The line largest_odd == z uses == which is a comparison operator. It should be an assignment

# Show the largest odd number from x, y and z 
print(f"For {x}, {y}, {z}, the largest odd number is: {largest_odd}") # if use {x, y, z},it's a tuple.Therefore, when printing, the console will display it in the tuple format like (1, 2, 5). 
#%% Exercise 7
# Ask the user for the type of conversion
conversion_type = int(input("Enter 1 for 12h to 24h conversion, or 2 for 24h to 12h conversion: "))

if conversion_type == 1:
    # 12h to 24h conversion
    hour = int(input("Enter the hour (1-12): "))
    minute = int(input("Enter the minutes (0-59): "))
    period = int(input("Enter 0 for AM or 1 for PM: "))

    # Convert to 24-hour format
    if period == 1 and hour != 12:
        hour += 12
    elif period == 0 and hour == 12:
        hour = 0

    # Print in 24-hour format
    print(f"The time in 24-hour format is {hour:02}:{minute:02}")

elif conversion_type == 2:
    # 24h to 12h conversion
    hour = int(input("Enter the hour (0-23): "))
    minute = int(input("Enter the minutes (0-59): "))

    # Determine period (AM/PM)
    period = "AM"
    if hour >= 12:
        period = "PM"
        if hour > 12:
            hour -= 12
    elif hour == 0:
        hour = 12

    # Print in 12-hour format
    print(f"The time in 12-hour format is {hour}:{minute:02} {period}")

else:
    print("Invalid input. Please enter 1 or 2.")
