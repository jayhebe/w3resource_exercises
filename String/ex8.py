def longest_word(word_list):
    words = sorted(word_list, key=len, reverse=True)
    return words[0]


if __name__ == '__main__':
    print(longest_word(["PHP", "Exercises", "Backend"]))
