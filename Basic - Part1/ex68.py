def sum_digits(number):
    s = number // 1000
    h = (number - s * 1000) // 100
    t = (number - s * 1000 - h * 100) // 10
    n = number % 10

    return s + h + t + n


if __name__ == '__main__':
    print(sum_digits(2345))
