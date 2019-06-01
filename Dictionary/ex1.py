sample_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(sorted(sample_dict.items(), key=lambda obj: obj[1]))
print(sorted(sample_dict.items(), key=lambda obj: obj[1], reverse=True))
