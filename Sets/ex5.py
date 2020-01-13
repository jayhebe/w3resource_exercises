s1 = {1, 2, 3, 4}
print(s1)
item = 2
if item in s1:
    s1.remove(item)

print(s1)

s1.discard(10)
print(s1)
