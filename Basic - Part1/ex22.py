# def count_four(number_list):
#     count = 0
#     for _ in number_list:
#         if _ == 4:
#             count += 1
#
#     return count


def count_four(number_list):
    return number_list.count(4)


if __name__ == '__main__':
    print(count_four([1, 3, 4, 5, 4, 6, 4]))
