def remove_dup_list(lst):
    return list(set(lst))


if __name__ == '__main__':
    print(remove_dup_list([10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]))
