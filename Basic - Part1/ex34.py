def sum_int(a, b):
    result = a + b
    if 15 <= result <= 20:
        return 20
    return result


if __name__ == '__main__':
    print(sum_int(7, 9))
    print(sum_int(7, 7))
