sample_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
# result = []
# start = 0
# for i in range(len(sample_list)):
#     if (i + 1) % 5 == 0:
#         result.append(sample_list[start:i + 1])
#         start = i + 1
#         if len(sample_list[start:]) < 5:
#             result.append(sample_list[start:])
#
# print(result)


def list_slice(lst, step):
    return [lst[i::step] for i in range(step)]


if __name__ == '__main__':
    print(list_slice(sample_list, 3))
