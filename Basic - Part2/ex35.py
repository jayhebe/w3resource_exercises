# params = list(map(int, input("Input the value of a, b, c, d, e, f:").split()))
a, b, c, d, e, f = [int(i) for i in input("Input the value of a, b, c, d, e, f: ").split()]
x = (c * e - b * f) / (a * e - b * d)
y = (c * d - a * f) / (b * d - a * e)
print(x, y)
