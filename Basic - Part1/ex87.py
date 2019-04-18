import os


def get_file_size(file_path):
    if os.path.isfile(file_path):
        return str(os.path.getsize(file_path)) + " bytes"


if __name__ == '__main__':
    print(get_file_size(r"C:/Study/Programming/Python/w3resource_exercises/Basic - Part1/ex84.py"))
