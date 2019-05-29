def circularly_identical(lst1, lst2):
    if len(lst1) == len(lst2):
        for item in lst1:
            if item not in lst2:
                return False
            else:
                continue
        return True
    return False


if __name__ == '__main__':
    print(circularly_identical([1, 2, 3, 4], [4, 3, 2, 1]))
    print(circularly_identical([1, 2, 3, 4], [4, 3]))
