sample_data = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_data = []
for tp in sample_data:
    tp = list(tp)
    tp[-1] = 100
    new_data.append(tuple(tp))

print(new_data)
