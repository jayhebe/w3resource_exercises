def list_to_int(lst):
    return int("".join([str(x) for x in lst]))


if __name__ == '__main__':
    print(list_to_int([11, 22, 33]))
    print(list_to_int([11, 33, 50]))
