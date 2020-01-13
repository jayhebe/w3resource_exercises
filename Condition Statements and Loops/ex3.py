"""
Write a Python program to guess a number between 1 to 9.
Note : User is prompted to enter a guess.
If the user guesses wrong then the prompt appears again until the guess is correct,
on successful guess, user will get a "Well guessed!" message, and the program will exit.
"""

import random

gold_number = random.randint(1, 9)
# print(gold_number)
while True:
    guess_number = int(input("Please guess a number between 1 to 9: "))
    if guess_number == gold_number:
        print("Well guessed!")
        break
    else:
        print("Sorry, please try again.")
