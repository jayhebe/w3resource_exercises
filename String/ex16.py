def insert_in_middle(src_str, char_str):
    middle_index = len(src_str) // 2

    return src_str[:middle_index] + char_str + src_str[middle_index:]


if __name__ == '__main__':
    print(insert_in_middle("{{}}", "Python"))
    print(insert_in_middle("[[[]]]", "PHP"))
