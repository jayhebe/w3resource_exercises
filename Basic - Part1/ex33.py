def sum_int(a, b, c):
    if a == b or a == c or b == c:
        return 0
    return a + b + c


if __name__ == '__main__':
    print(sum_int(2, 3, 4))
    print(sum_int(2, 2, 4))
