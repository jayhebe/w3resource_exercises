"""
Write a Python program to calculate a dog's age in dog's years.
Note: For the first two years, a dog year is equal to 10.5 human years.
After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15
The dog's age in dog's years is 73
"""


def get_dog_age(human_age):
    return human_age * 10.5 if human_age <= 2 else 2 * 10.5 + (human_age - 2) * 4


if __name__ == '__main__':
    human = int(input("Input a dog's age in human years: "))
    print("The dog's age in dog's years is {}".format(get_dog_age(human)))
