"""
Write a Python program to find numbers between 100 and 400 (both included)
where each digit of a number is an even number.
The numbers obtained should be printed in a comma-separated sequence.
"""

result = []
for num in range(100, 401):
    hundred = num // 100
    ten = num % 100 // 10
    digit = num % 10

    if hundred % 2 == 0 and ten % 2 == 0 and digit % 2 == 0:
        result.append(num)

print(", ".join([str(number) for number in result]))
