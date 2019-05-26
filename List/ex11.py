def common_member(lst1, lst2):
    lst1, lst2 = (lst2, lst1) if len(lst2) < len(lst1) else (lst1, lst2)
    for item in lst1:
        if item in lst2:
            return True

    return False


if __name__ == '__main__':
    print(common_member([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
    print(common_member([1, 2, 3, 4, 5], [6, 7, 8, 9]))
