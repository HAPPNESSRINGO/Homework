# -*- coding: utf-8 -*-
"""
Python Workshop 4 - Homework 3

@author: Yiyang Wang 999028285
"""
#%% Exercise 1
"""
b)
d)
e)
"""

#%% Exercise 2
# f)

#%% Exercise 3

# Original program
step = 0.2
accumulator = 0.0

while accumulator != 4.0:
	accumulator = accumulator + step
	print("I'm stuck here...")

print("The end!")

# Point 1
# Because of floating-point precision issues,accumulattor can never equal 4.0

# Point 2
# Change != to <
# It should be accumulator < 4.0

#%% Exercise 4
# get a positive integer
user_number = int(input("please input a positive integer:"))

# Initialize the accumulator and counter
total_sum = 0
current_number = 0

# Use a while loop 
while current_number <= user_number:
    total_sum += current_number
    current_number += 1

# Output the result
print("The result is:", total_sum)

#%% Exercise 5
# Get a positive integer
user_number = int(input("Please enter a positive integer: "))

# Initialize the accumulator and counter
total_sum = 0
current_number = 0

# Use a while loop t
while current_number <= user_number:
    # Check if current_number is a multiple of 7
    if current_number % 7 == 0:
        total_sum += current_number
    # Increment the counter
    current_number += 1

# Output the result
print("The result is:", total_sum)

#%% Exercise 6
# Initialize
fahrenheit = 0

# Use a while loop
while fahrenheit <= 120:
    # Convert Fahrenheit to Celsius using the formula and get the integer part
    celsius = int((5 / 9) * (fahrenheit - 32))
    # Print the  result
    print(f"{fahrenheit} F = {celsius} C")
    # += 10
    fahrenheit += 10

#%% Exercise 7
# Get a positive integer
user_number = int(input("Please enter a positive integer: "))

# Initialize
is_prime = True
divisor = 2

# Check if the number is less than 2 (not prime)
if user_number < 2:
    is_prime = False
else:
    # Use a while loop 
    while divisor <= user_number // 2:
        # If user_number is divisible by divisor, it is not a prime
        if user_number % divisor == 0:
            is_prime = False
            break
        # Increment the divisor to check the next possible factor
        divisor += 1

# Print the result
if is_prime:
    print(f"{user_number} is a prime number.")
else:
    print(f"{user_number} is not a prime number.")

#%% Exercise 8
# Get a positive integer
user_number = int(input("Please enter a positive integer: "))

# Initialize
guess = user_number / 2
iterations = 0

# Use Heron's method
while -0.1 < guess**2 - user_number < 0.1:
    guess = (guess + user_number / guess) / 2
    iterations += 1  

# Print the result
print(f"The approximate square root of {user_number} is {guess:.2f}")
print(f"Number of iterations: {iterations}")