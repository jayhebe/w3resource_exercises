"""
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""

import string


def upper_and_lower(s):
    count_upper = 0
    count_lower = 0
    for c in s:
        if c in string.ascii_uppercase:
            count_upper += 1
        if c in string.ascii_lowercase:
            count_lower += 1

    return count_upper, count_lower


if __name__ == '__main__':
    sample_str = "The quick Brow Fox"
    count_u, count_l = upper_and_lower(sample_str)
    print("No. of Upper case characters: {}".format(count_u))
    print("No. of Lower case characters: {}".format(count_l))
