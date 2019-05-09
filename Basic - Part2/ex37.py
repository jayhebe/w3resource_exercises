# count = 0
# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             for m in range(10):
#                 if i + j + k + m == 15:
#                     count += 1
#
# print(count)


import itertools
print("Input the number(n):")
n = int(input())
result = 0
for (i, j, k) in itertools.product(range(10), range(10), range(10)):
    result += (0 <= n - (i + j + k) <= 9)
print("Number of combinations:", result)
