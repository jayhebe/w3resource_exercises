def progression(num_list):
    a, b, c = num_list
    if b - a == c - b:
        return "arithmetic"

    if b / a == c / b:
        return "geometric "


if __name__ == '__main__':
    print(progression([3, 5, 7]))
    print(progression([2, 6, 18]))
