# def list_comp_num(lst, num):
#     for n in lst:
#         if n < num:
#             return False
#
#     return True


def list_comp_num(lst, num):
    return all(n > num for n in lst)


if __name__ == '__main__':
    print(list_comp_num([5, 6, 7, 8], 6))
    print(list_comp_num([5, 6, 7, 8], 3))
