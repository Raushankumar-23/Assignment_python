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
    file = open("sample.txt","r")

except:
    print("file does not exist") # file not exist execute

else:
    print("file is exists")
finally:
    print("thank") # its always execute

# content = file.read() # read full content
# print(content)

# print(file.tell())
# file.seek(0)         # cursur reset initial point

count = len(file.readlines())
for con in range(0,count):
    print(file.readline())

print(file.tell())
file.seek(0)         # cursur reset initial point

content1 = file.readline().split() # read content  word by word
for con in content1:
    print(con)

file.seek(0)



file.close()