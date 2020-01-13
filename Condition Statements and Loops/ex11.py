"""
Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
"""

m = int(input("Please enter the row: "))
n = int(input("Please enter the column: "))

result = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(i * j)
    result.append(row)

print(result)
