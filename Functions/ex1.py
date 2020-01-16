"""
Write a Python function to find the Max of three numbers.
"""


def max_num(a, b, c):
    max_n = (a if a > b else b)
    return max_n if max_n > c else c


if __name__ == '__main__':
    print(max_num(2, 5, 8))
