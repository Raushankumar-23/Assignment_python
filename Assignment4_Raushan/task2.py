"""
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""

text = input("Enter text to write in file : ")


with open("output.txt","a+") as file:
    if file.write(text + "\n"):
        print("Data successfully written to output.txt")

    else:
        print("Written failed")

    text1 = input("Enter additional text to append : ")
    if file.write(text1 +"\n"):
        print("Data successfully append")

    else:
        print("append failed")

    file.seek(0)
    content = file.read()
    print(content)









