result = []
temp = []
for i in range(1, 21):
    if i % 5 == 0:
        result.append(temp)
        temp = []
    temp.append(i)

print(result)
