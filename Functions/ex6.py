"""
Write a Python function to check whether a number is in a given range.
"""


def is_range(n, low, high):
    if n in range(low, high + 1):
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_range(3, 4, 8))
    print(is_range(9, 2, 20))
