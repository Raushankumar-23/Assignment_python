"""
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
"""

num = int(input("Enter a number : "))

if num >0:
    if num % 2 == 0:
        print(num, "is Even Number")
    else:
        print(num, "is odd number")

else:
    print("please enter number grater than 0")
