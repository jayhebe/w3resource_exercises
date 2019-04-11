import math


def get_sphere_volume(radius):
    return 4 / 3 * math.pi * math.pow(radius, 3)


if __name__ == '__main__':
    print(get_sphere_volume(6))
