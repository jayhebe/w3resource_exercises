sample_data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result_data = {}
for dt in sample_data:
    result_data.setdefault(dt["item"], 0)
    result_data[dt["item"]] += dt["amount"]

print(result_data)
