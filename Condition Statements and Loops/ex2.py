"""
Write a Python program to convert temperatures to and from celsius, fahrenheit.
[ Formula : c/5 = (f-32)/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""


def f2c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def c2f(celsius):
    return celsius * 9 / 5 + 32


if __name__ == '__main__':
    print(c2f(60))
    print(f2c(45))
