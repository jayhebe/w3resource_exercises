"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""


def unique_list(lst):
    return list(set(lst))


if __name__ == '__main__':
    sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
    print(unique_list(sample_list))
