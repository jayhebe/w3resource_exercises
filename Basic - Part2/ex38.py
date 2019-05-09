def is_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    print("Input the number(n): ")
    n = int(input())
    count = 0
    if n == 1:
        print("Number of prime numbers which are less than or equal to n:", count)
    else:
        for num in range(2, n):
            if is_prime(num):
                count += 1
        print("Number of prime numbers which are less than or equal to n:", count)
