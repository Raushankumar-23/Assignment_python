"""
Task 2: Using the Math Module for Calculations

Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.

"""

import math

num = int(input("Enter a number  : "))

square_root = math.sqrt(num) #square root
natural_log = math.log(num) # natural log

radian = math.radians(num) # convert into radian
sine_of = math.sin(radian)

print(f"the Square root of {num} is {square_root}")
print(f"the natural log of {num} is {natural_log}")
print(f"The sine vale of {num} is {sine_of}")