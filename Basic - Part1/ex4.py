import math


def calc_area(r):
    return math.pi * r * r


if __name__ == '__main__':
    radius = float(input("Please enter the radius of a cycle: "))
    print("r = {}".format(radius))
    print("Area = {}".format(calc_area(radius)))
