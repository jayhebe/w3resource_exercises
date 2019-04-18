import os


def file_or_dir(path):
    if os.path.isfile(path):
        print("Is a file")
    elif os.path.isdir(path):
        print("Is a directory.")


if __name__ == '__main__':
    file_or_dir(r"C:/Study/Programming/Python/w3resource_exercises/Basic - Part1/ex84.py")
    file_or_dir(r"C:/Study/Programming/Python/w3resource_exercises/Basic - Part1")
