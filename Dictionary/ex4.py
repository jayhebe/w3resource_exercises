def is_exist(key, dic):
    if key in dic.keys():
        return True
    else:
        return False


if __name__ == '__main__':
    d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    print(is_exist(5, d))
    print(is_exist(7, d))
