def max_length_zero(bin_str):
    for i in range(len(bin_str), 0, -1):
        if "0" * i in bin_str:
            return i


if __name__ == '__main__':
    print(max_length_zero("111000010000110"))
    print(max_length_zero("111000111"))
