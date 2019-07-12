sample_data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sorted(sample_data, key=lambda obj: obj[1], reverse=True))
