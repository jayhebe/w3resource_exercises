"""
Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""


def sum_num(lst):
    sum_n = 0
    for i in lst:
        sum_n += i
    return sum_n


if __name__ == '__main__':
    t = (8, 2, 3, 0, 7)
    print(sum_num(t))
