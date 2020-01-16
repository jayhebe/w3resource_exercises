"""
Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and
that has no positive divisors other than 1 and itself.
"""


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(is_prime(3))
    print(is_prime(7))
    print(is_prime(8))
    print(is_prime(15))
    print(is_prime(17))
