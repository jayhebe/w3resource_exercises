def second_largest(num_list):
    return sorted(set(num_list), reverse=True)[1]


if __name__ == '__main__':
    print(second_largest([1, 2, 3, 4, 4]))
    print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
