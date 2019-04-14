def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_even(2))
    print(is_even(6))
    print(is_even(7))
    print(is_even(256))
