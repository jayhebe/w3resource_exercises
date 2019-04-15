# import sys
#
#
# print(sys.version)


import struct


# struct.calcsize("P") -> return how many bytes an integer uses
print(struct.calcsize("P") * 8)
