d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

for k, v in d2.items():
    if k in d1.keys():
        d1[k] += v
    else:
        d1.update({k: v})

print(d1)
