def smallest_largest(sentence):
    result = {}
    words = sentence.split()
    for word in words:
        result[word] = len(word)

    result = sorted(result.items(), key=lambda item: item[1], reverse=True)

    return result[0][0], result[-1][0]


if __name__ == '__main__':
    print(smallest_largest("Write a Java program to sort an array of given integers using Quick sort Algorithm"))
