"""
Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""


def print_even(lst):
    return lst[1::2]


if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(print_even(sample_list))
