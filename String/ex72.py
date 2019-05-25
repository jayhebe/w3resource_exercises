import itertools


def remove_consecutive_duplicates(s1):
    return ''.join(i for i, _ in itertools.groupby(s1))


str1 = "aabcdaee"
print("Original String: ", str1)
print("\nRemoving all consecutive duplicates:")
print(remove_consecutive_duplicates(str1))
