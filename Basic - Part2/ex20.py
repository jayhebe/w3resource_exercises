# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fac(n - 1)
#
#
# if __name__ == '__main__':
#     result = str(fac(100))[::-1]
#     for i in range(len(result)):
#         if result[i] != "0":
#             print(i)
#             break


def factendzero(n):
    x = n // 5
    y = x
    while x > 0:
        x /= 5
        y += int(x)
    return y


print(factendzero(5))
print(factendzero(12))
print(factendzero(100))
