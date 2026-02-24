"""
ASSIGNMENT 5:
Module 6: Data Structures and Strings in Python

Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.


"""
from tkinter.font import names

students = {
    "Rohit": 85,
    "Amit": 78,
    "Neha": 92,
    "Priya": 88,
    "Rahul": 76,
    "Sneha": 90
}

name = input("Enter student's name : ")

for s1,s2 in students.items():
    if s1.lower() == name.lower():
        print(s1+"'s","marks",s2)


#print(students)