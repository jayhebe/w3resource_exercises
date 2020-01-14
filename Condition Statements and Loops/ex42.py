"""
Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
"""

numbers = []
while True:
    num = int(input("Please enter an integer number (0 to exit): "))
    if num == 0:
        break
    numbers.append(num)

print("The sum of numbers is {}".format(sum(numbers)))
print("The average of numbers is {}".format(sum(numbers) / len(numbers)))
