"""
Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
"""


def add(a, b):
    return 20 if 15 < a + b < 20 else a + b


x = 7
y = 10
print(add(x, y))
