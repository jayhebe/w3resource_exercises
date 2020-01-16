"""
Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""


def mul_num(lst):
    mul_n = 1
    for i in lst:
        mul_n *= i
    return mul_n


if __name__ == '__main__':
    t = (8, 2, 3, -1, 7)
    print(mul_num(t))
