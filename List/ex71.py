list1 = [{}, {}, {}]
list2 = [{1, 2}, {}, {}]
print(all(len(i) == 0 for i in list1))
print(all(len(i) == 0 for i in list2))
