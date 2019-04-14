# def diff_color(list1, list2):
#     new_list = []
#     for color in list1:
#         if color not in list2:
#             new_list.append(color)
#
#     return set(new_list)
#
#
# if __name__ == '__main__':
#     color_list_1 = {"White", "Black", "Red"}
#     color_list_2 = {"Red", "Green"}
#     print(diff_color(color_list_1, color_list_2))


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))
