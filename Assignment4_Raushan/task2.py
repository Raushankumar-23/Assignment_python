"""
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""

text = input("Enter text to write in file: ")

with open("output.txt", "w+") as file:
    file.write(text + "\n")
    print("Data successfully written to output.txt")

    text1 = input("Enter additional text to append: ")
    file.write(text1 + "\n")
    print("Data successfully appended")

    file.seek(0)  # cursor to beginning
    print("\nFinal File Content:")
    print(file.read())