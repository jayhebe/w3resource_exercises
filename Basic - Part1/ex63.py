import os


def get_abs_path(filename):
    return os.path.abspath(filename)


if __name__ == '__main__':
    print(get_abs_path(r".\ex63.py"))
