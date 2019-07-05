sample_data = "w3resource"
result_data = {}
for ch in sample_data:
    result_data.setdefault(ch, 0)
    result_data[ch] += 1

print(result_data)
