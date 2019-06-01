def replace_last_ele(lst1, lst2):
    # lst1.pop(-1)
    # lst1.extend(lst2)
    # return lst1
    lst1[-1:] = lst2
    return lst1


if __name__ == '__main__':
    print(replace_last_ele([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))
