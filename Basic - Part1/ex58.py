def sum_int(n):
    result = 0
    for _ in range(n + 1):
        result += _

    return result


if __name__ == '__main__':
    print(sum_int(20))
