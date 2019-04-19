import os


def get_filenname(path):
    return os.path.basename(path)


if __name__ == '__main__':
    print(get_filenname(r"C:/Study/Programming/Python/w3resource_exercises/Basic - Part1/ex102.py"))
