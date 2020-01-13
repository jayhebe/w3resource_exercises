"""
Write a Python program that accepts a sequence of lines (blank line to terminate) as input
and prints the lines as output (all characters in lower case).
"""

result = []
while True:
    line = input("Please input anything you want to say: ").strip()
    if len(line) == 0:
        break
    else:
        result.append(line)

for line in result:
    print(line.lower())
