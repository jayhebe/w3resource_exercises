def is_empty_list(lst):
    if len(lst) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_empty_list([]))
    print(is_empty_list([1, 2, 3]))
