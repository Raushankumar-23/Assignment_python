"""
ASSIGNMENT 4:
Module 5: Files, Exceptions, and Errors in Python

Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

"""

try:
    with open("sample.txt", "r") as file:
        print("File exists\n")

        # Print line by line
        for line in file:
            print(line.strip())

        # Reset cursor
        file.seek(0)

        print("\nWord by word:")
        for word in file.read().split():
            print(word)

except FileNotFoundError:
    print("File does not exist")

finally:
    print("\nThank you")