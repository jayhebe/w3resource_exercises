"""
Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
"""


def reverse_str(s):
    return s[::-1]


if __name__ == '__main__':
    test_str = "1234abcd"
    print(reverse_str(test_str))
