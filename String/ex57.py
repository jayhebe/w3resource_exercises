# def remove_spaces(char_str):
#     chars = list(char_str)
#     for i in range(len(chars)):
#         if " " in chars:
#             chars.remove(" ")
# 
#     return "".join(chars)


def remove_spaces(char_str):
    return char_str.replace(" ", "")


if __name__ == '__main__':
    print(remove_spaces("This is a test string"))
