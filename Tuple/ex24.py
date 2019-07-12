sample_data = [10, 20, 30, (10, 20), 40]
count = 0
for item in sample_data:
    if not isinstance(item, tuple):
        count += 1
    else:
        break

print(count)
