"""
Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument.
"""


def fac(num):
    fac_n = 1
    for i in range(2, num + 1):
        fac_n *= i
    return fac_n


if __name__ == '__main__':
    print(fac(6))
    print(fac(8))
