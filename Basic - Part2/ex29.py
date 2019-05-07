def common_divisors(a, b):
    x, y = min(a, b), max(a, b)
    divisors = []
    for i in range(1, x + 1):
        if a % i == 0 and b % i == 0:
            divisors.append(i)
            i += 1

    return divisors


if __name__ == '__main__':
    print(common_divisors(2, 4))
    print(common_divisors(2, 8))
    print(common_divisors(12, 24))
