def word_count(sentence):
    words = sentence.split()
    result = {}
    for word in words:
        result.setdefault(word, 0)
        result[word] += 1

    return result


if __name__ == '__main__':
    print(word_count("the quick brown fox jumps over the lazy dog."))
