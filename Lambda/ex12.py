"""
Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
"""

array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
print("Original arrays:")
print(array_nums)
result = [x for x in array_nums if x < 0] + [x for x in array_nums if x >= 0]
print("\nRearrange positive and negative numbers of the said array:")
print(result)
