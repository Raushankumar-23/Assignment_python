"""
Task 2: Demonstrate List Slicing
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

"""

list1 = [1,2,3,4,5,6,7,8,9,10]     #Creates a list of numbers from 1 to 10.

first_five = list1[0:5]
print(f"first five element of list1 is {first_five}") #the first five elements from the list

rev = first_five[::-1] #Reverses these extracted elements.
print(f"reversed extracted list {rev}")