# def get_sum(a, b, c):
#     if a == b == c:
#         return (a + b + c) * 3
#     else:
#         return a + b + c


def get_sum(a, b, c):
    result = a + b + c

    if a == b == c:
        result *= 3

    return result


if __name__ == '__main__':
    x, y, z = input("Please enter 3 numbers seperated by comma: ").split(",")
    print(get_sum(int(x), int(y), int(z)))
