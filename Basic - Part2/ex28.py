tn = int(input("Input third term of the series: "))
tltn = int(input("Input 3rd last term: "))
s_sum = int(input("Sum of the series: "))
n = int(2 * s_sum / (tn + tltn))
print("Length of the series: ", n)
d = (tltn - tn) / (n - 5)
a = tn - 2 * d
j = 0
print("Series:")
for j in range(n - 1):
    print(int(a), end=" ")
    a += d
print(int(a), end=" ")
