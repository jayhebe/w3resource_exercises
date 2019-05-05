import math


def get_side(a, b):
    return math.sqrt(a ** 2 + b ** 2)


if __name__ == '__main__':
    print(get_side(3, 4))
    print(get_side(9, 16))
