sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
result = []
for item in sample_list:
    if item not in result:
        result.append(item)

print(result)
