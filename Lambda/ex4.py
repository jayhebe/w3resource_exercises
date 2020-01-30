"""
Write a Python program to sort a list of dictionaries using Lambda.
"""

models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
models.sort(key=lambda obj: obj["color"])
print(models)
