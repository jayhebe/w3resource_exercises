import math


def get_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


if __name__ == '__main__':
    print(get_distance((1, 5), (2, 6)))
    print(get_distance((4, 0), (6, 6)))
