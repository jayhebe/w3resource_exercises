def count_carry(a, b):
    carry = 0
    for x, y in zip(str(a), str(b)):
        if int(x) + int(y) >= 10:
            carry += 1

    return carry


if __name__ == '__main__':
    print(count_carry(563, 789))
    print(count_carry(786, 457))
    print(count_carry(5, 6))
