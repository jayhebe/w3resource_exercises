# def check_lower_letter(s):
#     for ch in s:
#         if ch.islower():
#             return True
#
#     return False


def check_lower_letter(s):
    return any(ch.islower() for ch in s)


if __name__ == '__main__':
    print(check_lower_letter("SSSSSsSSSS"))
    print(check_lower_letter("SSSSSASSSS"))
