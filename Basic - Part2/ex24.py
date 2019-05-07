def num_of_divisors(number):
    count = 0
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            count += 1

    return count


if __name__ == '__main__':
    print(num_of_divisors(15))
    print(num_of_divisors(12))
    print(num_of_divisors(9))
    print(num_of_divisors(6))
    print(num_of_divisors(3))
