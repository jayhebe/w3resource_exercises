import math


def calc_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


if __name__ == '__main__':
    print(calc_hypotenuse(4.0, 3.0))
