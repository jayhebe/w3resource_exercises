"""
Write a Python program to check the validity of password input by users.
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""

import string


def is_valid_password(pwd):
    if len(pwd) > 16 or len(pwd) < 6:
        return False

    count_letters = 0
    count_numbers = 0
    count_specials = 0

    for c in pwd:
        if c in string.ascii_letters:
            count_letters += 1
        elif c in string.digits:
            count_numbers += 1
        elif c in "$#@":
            count_specials += 1

    if count_numbers == 0:
        return False

    if count_letters == 0:
        return False

    if count_specials == 0:
        return False

    return True


if __name__ == '__main__':
    password = input("Please enter a password: ")
    if is_valid_password(password):
        print("Valid password")
    else:
        print("Invalid password")
