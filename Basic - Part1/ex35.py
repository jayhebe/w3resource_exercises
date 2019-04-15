def equal_or_five(a, b):
    if a == b or a + b == 5 or abs(a - b) == 5:
        return True
    else:
        return False


if __name__ == '__main__':
    print(equal_or_five(3, 3))
    print(equal_or_five(3, 2))
    print(equal_or_five(10, 5))
    print(equal_or_five(5, 10))
    print(equal_or_five(10, 3))
