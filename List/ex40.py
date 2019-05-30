from itertools import groupby
# from operator import itemgetter


def split_word(word_list):
    transform = {}
    extract = [(k, list(v)) for k, v in groupby(word_list, key=lambda word: word[0])]
    for key, value in extract:
        transform.setdefault(key, [])
        transform[key] += value

    return transform


# def split_word(word_list):
#     for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
#         print(letter)
#         for w in words:
#             print(w)


if __name__ == '__main__':
    wd_lst = [
        'be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
        'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call'
    ]
    print(split_word(wd_lst))
