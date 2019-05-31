def insert_ele(lst, ele):
    i = 0
    while i < len(lst):
        lst.insert(i, ele)
        i += 2
    return lst


if __name__ == '__main__':
    print(insert_ele(['Red', 'Green', 'Black'], "c"))
