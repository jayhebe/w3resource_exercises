# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#
# newlst = lst[:]
# while len(newlst) != 0:
#     n = 0
#     while n < len(newlst):
#         if (n + 1) % 3 == 0:
#             print(lst.pop(n), end=" ")
#         n += 1
#     newlst = lst[:]


def remove_nums(int_list):
    position = 2
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        idx = (position + idx) % len_list
        print(int_list.pop(idx))
        len_list -= 1


nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
remove_nums(nums)
