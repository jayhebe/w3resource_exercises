def second_smallest(num_list):
    return sorted(set(num_list))[1]


if __name__ == '__main__':
    print(second_smallest([1, 2, -8, -2, 0, -2]))
    print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
    print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
