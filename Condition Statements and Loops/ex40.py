"""
Write a Python program to find the median of three values.
Expected Output:

Input first number: 15
Input second number: 26
Input third number: 29
The median is 26.0
"""


def find_median(a, b, c):
    return list(sorted([a, b, c]))[1]


x = input("Input first number: ")
y = input("Input second number: ")
z = input("Input third number: ")

print("The median is {}".format(find_median(x, y, z)))
