from itertools import product

sample_data = {'1': ['a', 'b'], '2': ['c', 'd']}
for item in product(*list(sample_data.values())):
    print("".join(item))
