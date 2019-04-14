def print_histogram(number_list, his_chr):
    for number in number_list:
        print(his_chr * number)


if __name__ == '__main__':
    print_histogram([2, 3, 4, 6], "@")
    print_histogram([1, 3, 7, 5], "!")
