from difflib import SequenceMatcher


def longest_common_sub(char_str1, char_str2):
    seq_match = SequenceMatcher(None, char_str1, char_str2)
    match = seq_match.find_longest_match(0, len(char_str1), 0, len(char_str2))

    if match.size != 0:
        return char_str1[match.a: match.a + match.size]
    else:
        return "Longest common sub-string not present"


if __name__ == '__main__':
    print(longest_common_sub("abcdefgh", "xswerabcdwd"))
