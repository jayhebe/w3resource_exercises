"""
Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
"""


import string


def is_pangram(sentence):
    letter_table = {}
    for letter, count in zip(string.ascii_lowercase, [0] * 26):
        letter_table[letter] = count

    for c in sentence:
        if c in letter_table.keys():
            letter_table[c] += 1

    if 0 not in letter_table.values():
        return True
    else:
        return False


def is_pangram_sample(sentence):
    return set(sentence.lower()) >= set(string.ascii_lowercase)


if __name__ == '__main__':
    s1 = "The quick brown fox jumps over the lazy dog"
    s2 = "are you OK"
    print(is_pangram(s1))
    print(is_pangram(s2))

    print(is_pangram_sample(s1))
    print(is_pangram_sample(s2))
