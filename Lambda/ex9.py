"""
Write a Python program to check whether a given string is number or not using Lambda.
"""

is_number = lambda x: True if x.isdigit() else False
print(is_number("22"))
print(is_number("2b"))
