def count_range_in_list(li, small, big):
    ctr = 0
    for x in li:
        if small <= x <= big:
            ctr += 1
    return ctr


list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
print(count_range_in_list(list1, 40, 100))

list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(count_range_in_list(list2, 'a', 'e'))
