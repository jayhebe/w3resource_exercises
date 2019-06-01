def insert_str(lst, s):
    return [s + str(n) for n in lst]


if __name__ == '__main__':
    print(insert_str([1, 2, 3, 4], "emp"))
