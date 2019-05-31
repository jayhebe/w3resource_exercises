lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([x for x in lst if x % 2 == 1])
print(list(filter(lambda x: x % 2 == 1, lst)))
