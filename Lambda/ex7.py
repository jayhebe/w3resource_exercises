"""
Write a Python program to find if a given string starts with a given character using Lambda.
"""

start = lambda x, y: True if x.startswith(y) else False
print(start("Java", "P"))
print(start("Python", "P"))
