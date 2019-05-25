def move_spaces(str1):
    no_spaces = [char for char in str1 if char != ' ']
    space = len(str1) - len(no_spaces)
    # Create string with spaces
    result = ' ' * space
    return result + ''.join(no_spaces)


s1 = "Python Exercises"
print("Original String:\n", s1)

print("\nAfter moving all spaces to the front:")
print(move_spaces(s1))
