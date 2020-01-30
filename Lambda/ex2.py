"""
Write a Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number.
"""


def compute(n):
    return lambda x: x * n


result = compute(2)
print(result(15))
result = compute(3)
print(result(15))
