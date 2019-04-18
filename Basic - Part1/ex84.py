# def count_spec_chr(s, c):
#     count = 0
#     for ch in s:
#         if ch == c:
#             count += 1
#
#     return count


def count_spec_chr(s, c):
    return s.count(c)


if __name__ == '__main__':
    print(count_spec_chr("This is a specific string", "i"))
