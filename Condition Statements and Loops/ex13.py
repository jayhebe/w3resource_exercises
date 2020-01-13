"""
Write a Python program which accepts a sequence of comma separated 4 digit binary numbers
as its input and print the numbers that are divisible by 5 in a comma separated sequence.
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010
"""

result = []
bins = input("Please enter sample data: ").split(",")
for b in bins:
    number = int(b, 2)
    if number % 5 == 0:
        result.append(b)

print(", ".join(result))
