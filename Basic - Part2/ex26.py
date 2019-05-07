def absolute_diff(num_list):
    result = 0
    for f_num in num_list:
        for s_num in num_list[num_list.index(f_num) + 1:]:
            # print(f_num, s_num)
            result += (s_num - f_num)

    return result


if __name__ == '__main__':
    print(absolute_diff([1, 2, 3]))
    print(absolute_diff([1, 4, 5]))
