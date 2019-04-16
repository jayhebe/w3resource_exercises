def get_midpoint(point1, point2):
    return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2


if __name__ == '__main__':
    print(get_midpoint((2, 2), (4, 4)))
