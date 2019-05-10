def str_length(s):
    count = 0
    for _ in s:
        count += 1

    return count


if __name__ == '__main__':
    print(str_length("123"))
    print(str_length("hello, world"))
