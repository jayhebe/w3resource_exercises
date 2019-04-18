def copy_code(file_path):
    with open(file_path) as fp:
        for line in fp.readlines():
            print(line, end="")


if __name__ == '__main__':
    copy_code(r".\ex90.py")
