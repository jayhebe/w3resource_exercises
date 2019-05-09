# def is_right_triangle(a, b, c):
#     sides = [a, b, c]
#     hypotenuse = max(a, b, c)
#     sides.remove(hypotenuse)
#     if sides[0] ** 2 + sides[1] ** 2 == hypotenuse ** 2:
#         return "Yes"
#     else:
#         return "No"


def is_right_triangle(a, b, c):
    x, y, z = sorted([a, b, c])
    if x ** 2 + y ** 2 == z ** 2:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    print(is_right_triangle(8, 7, 6))
    print(is_right_triangle(3, 4, 5))
