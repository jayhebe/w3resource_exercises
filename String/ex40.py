def reverse_word(word_str):
    word_list = word_str.split()
    return " ".join(word_list[::-1])


if __name__ == '__main__':
    print(reverse_word("The quick brown fox"))
    print(reverse_word("Python Exercises"))
