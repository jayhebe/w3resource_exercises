def get_median(a, b, c):
    x = max(a, b, c)
    y = min(a, b, c)

    return a + b + c - x - y


if __name__ == '__main__':
    print(get_median(25, 15, 35))
    print(get_median(33, 25, 45))
