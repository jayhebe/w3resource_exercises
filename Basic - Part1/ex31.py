def get_gcd(a, b):
    small_one = min(a, b)
    for divisor in reversed(range(1, small_one + 1)):
        if a % divisor == 0 and b % divisor == 0:
            return divisor


if __name__ == '__main__':
    print(get_gcd(12, 18))
    print(get_gcd(12, 13))
    print(get_gcd(12, 36))
