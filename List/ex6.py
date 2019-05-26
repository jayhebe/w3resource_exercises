def sort_tuple_list(tuple_list):
    return sorted(tuple_list, key=lambda t: t[1])


if __name__ == '__main__':
    print(sort_tuple_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
