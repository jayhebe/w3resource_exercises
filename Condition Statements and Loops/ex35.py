"""
Write a Python program to check a string represent an integer or not.
Expected Output:

Input a string: Python
The string is not an integer.
"""

string = input("Input a string: ")
if string.isdigit():
    print("The string is an integer.")
else:
    print("The string is not an integer.")
