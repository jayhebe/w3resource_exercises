"""
Write a Python program to construct the following pattern, using a nested loop number.
Expected Output:

1
22
333
4444
55555
666666
7777777
88888888
999999999
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, end="")
        if i == j:
            print()
            break

# for i in range(10):
#     print(str(i) * i)
