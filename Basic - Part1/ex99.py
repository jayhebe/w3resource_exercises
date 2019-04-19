import sys
import time
import os


print("This sentence will be disappear.")
time.sleep(5)
os_ver = sys.platform
# os_ver = os.name
# if os_ver == "nt":
#     os.system("cls")
# elif os_ver == "posix":
#     os.system("clear")

if os_ver == "win32":
    os.system("cls")
elif os_ver == "linux":
    os.system("clear")
