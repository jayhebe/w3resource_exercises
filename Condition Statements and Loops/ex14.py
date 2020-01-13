"""
Write a Python program that accepts a string and calculate the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2
"""

count_letter = 0
count_digits = 0
data = input("Please enter sample data: ")
for c in data:
    if c.isalpha():
        count_letter += 1
    elif c.isdigit():
        count_digits += 1

print("Letters: {}".format(count_letter))
print("Digits: {}".format(count_digits))
