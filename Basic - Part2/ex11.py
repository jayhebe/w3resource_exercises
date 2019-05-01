x = [10, 20, 20, 20, 20]
y = [10, 20, 30, 40, 30]
z = [10, 30, 40, 20, 20]
target = 70

result = []
for a, b, c in zip(x, y, z):
    if a + b + c == target:
        result.append((a, b, c))

print(result)
