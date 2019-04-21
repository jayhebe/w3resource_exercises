from functools import reduce


x = 8
print(reduce(lambda a, b: a + b ** 3, range(x)))
