"""
Write a Python program to execute a string containing Python code.
"""


def exec_code(s):
    return exec(s)


if __name__ == '__main__':
    sample_str = "print('hello')"
    code = """
def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is:', mutiply(2,3))
"""
    exec_code(sample_str)
    exec_code(code)
