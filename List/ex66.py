sample_list = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(sorted(sample_list, key=max, reverse=True)[0])
print(max(sample_list, key=sum))
