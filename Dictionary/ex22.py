my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
print(sorted([(k, v) for k, v in my_dict.items()], key=lambda obj: obj[1], reverse=True)[:3])
