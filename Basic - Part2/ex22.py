def seq_num(index):
    if 0 <= index - 1 < 4:
        return 1
    else:
        return seq_num(index - 1) + seq_num(index - 2) + seq_num(index - 3) + seq_num(index - 4)


if __name__ == '__main__':
    print(seq_num(5))
    print(seq_num(6))
