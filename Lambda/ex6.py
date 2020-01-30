"""
Write a Python program to square and cube every number in a given list of integers using Lambda.
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = lambda x: x ** 2
cube = lambda x: x ** 3

print([square(num) for num in nums])
print([cube(num) for num in nums])
