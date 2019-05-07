def is_palindrome(str_num):
    if str_num == str_num[::-1]:
        return True
    else:
        return False


def reverse_add(str_num):
    return str(int(str_num) + int(str_num[::-1]))


if __name__ == '__main__':
    num = "19"
    while not is_palindrome(num):
        num = reverse_add(num)
    print(num)
