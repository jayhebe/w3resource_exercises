"""
Write a Python function that checks whether a passed string is palindrome or not
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
"""


def is_palindrome(sentence):
    sentence = sentence.replace(" ", "")
    if sentence == sentence[::-1]:
        return True
    return False


if __name__ == '__main__':
    print(is_palindrome("madam"))
    print(is_palindrome("nurses run"))
