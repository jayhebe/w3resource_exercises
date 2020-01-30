"""
Write a Python program to sort a list of tuples using Lambda.
"""

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(list(sorted(subject_marks, key=lambda obj: obj[0])))
print(list(sorted(subject_marks, key=lambda obj: obj[1])))
