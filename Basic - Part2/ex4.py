lst = [1, -6, 4, 2, -1, 2, 0, -2, 0]
n = 0

while n + 2 < len(lst):
    if lst[n] + lst[n + 1] + lst[n + 2] == 0:
        print(lst[n], lst[n + 1], lst[n + 2])
    n += 1
