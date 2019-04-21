import os
import sys
import platform


print("Operating system name: ", end="")
print(os.name)
print("Platform name: ", end="")
print(sys.platform)
print("Platform release: ", end="")
print(platform.release())
