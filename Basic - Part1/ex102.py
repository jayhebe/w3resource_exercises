import subprocess


result = subprocess.check_output("ipconfig", shell=True, universal_newlines=True)
print(result)
