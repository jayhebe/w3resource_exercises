def sort_int(a, b, c):
    x = min(a, b, c)
    y = max(a, b, c)
    z = (a + b + c) - x - y

    return x, z, y


if __name__ == '__main__':
    print(sort_int(2, 8, 5))
    print(sort_int(6, 5, 4))
