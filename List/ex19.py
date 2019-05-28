# def list_diff(lst1, lst2):
#     result = []
#     lst1, lst2 = (lst1, lst2) if len(lst1) > len(lst2) else (lst2, lst1)
#     for l in lst1:
#         if l not in lst2:
#             result.append(l)
#
#     return result


def list_diff(lst1, lst2):
    lst1, lst2 = (lst1, lst2) if len(lst1) > len(lst2) else (lst2, lst1)
    return list(set(lst1) - set(lst2))


if __name__ == '__main__':
    print(list_diff([1, 2, 1], [1, 2, 3, 4]))
    print(list_diff([1, 2], [1, 2, 3, 4]))
    print(list_diff([1, 2, 3, 4], [1, 2]))
