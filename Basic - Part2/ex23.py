def times_to_subtract(num):
    result = 0
    while num > 0:
        num -= sum([int(i) for i in list(str(num))])
        result += 1

    return result


if __name__ == '__main__':
    print(times_to_subtract(9))
    print(times_to_subtract(21))
