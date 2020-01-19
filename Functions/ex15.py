"""
Write a Python program that accepts a hyphen-separated sequence of words as input
and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
"""


def sorted_words(sequence):
    words = sequence.split("-")
    return "-".join(list(sorted(words)))


if __name__ == '__main__':
    test_sequence = "green-red-yellow-black-white"
    print(sorted_words(test_sequence))
