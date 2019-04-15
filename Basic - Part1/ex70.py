import os

folder = r"C:\Study\Programming\Python\Python_Programming"
files = [os.path.sep.join([folder, file]) for file in os.listdir(folder) if file.endswith(".py")]
files.sort(key=os.path.getctime)
print(files)
