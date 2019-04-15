def get_lcm(a, b):
    big_one = max(a, b)
    for multiple in range(big_one, a * b + 1):
        if multiple % a == 0 and multiple % b == 0:
            return multiple


if __name__ == '__main__':
    print(get_lcm(12, 18))
    print(get_lcm(12, 13))
    print(get_lcm(12, 36))
