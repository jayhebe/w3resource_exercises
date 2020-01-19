"""
Write a Python function to create and print a list
where the values are square of numbers between 1 and 30 (both included).
"""


def print_values():
    print([i ** 2 for i in range(1, 31)])


if __name__ == '__main__':
    print_values()
