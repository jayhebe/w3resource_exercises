sample_data = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
for i, t in sorted([(k, v) for k, v in sample_data.items()], key=lambda obj: obj[1], reverse=True)[:3]:
    print(i, t)
