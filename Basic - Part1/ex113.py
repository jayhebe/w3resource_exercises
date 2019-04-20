number = input("Please input a number: ")

try:
    print(float(number))
except TypeError:
    print("This is not a number")
