# import os
#
#
# def file_exists(filename):
#     if os.path.exists(filename):
#         return True
#     else:
#         return False


def file_exists(filename):
    try:
        with open(filename) as fp:
            return True
    except:
        return False


if __name__ == '__main__':
    print(file_exists(r".\ex40.py"))
    print(file_exists(r".\lalala.py"))
