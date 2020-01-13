"""
Write a Python program that accepts a word from the user and reverse it.
"""

word = input("Please enter a word: ")
print("".join(list(reversed(word))))
print("".join(word[::-1]))
