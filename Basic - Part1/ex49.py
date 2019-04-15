import os


def list_all_files(directory):
    file_list = []
    for item in os.listdir(directory):
        if os.path.isfile(os.path.sep.join([directory, item])):
            file_list.append(item)

    return file_list


if __name__ == '__main__':
    print(list_all_files(r"C:\Study\Programming\Python\Python_Programming"))
