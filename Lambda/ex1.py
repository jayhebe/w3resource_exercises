"""
Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and print the result.
"""

lbd = lambda x: x + 15
print(lbd(10))
lbd = lambda x, y: x * y
print(lbd(6, 18))
