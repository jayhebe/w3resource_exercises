import sys


print("file name: ", sys.argv[0])
print("argument number: ", len(sys.argv[1:]))
print("argument(s):")
for arg in sys.argv[1:]:
    print(arg)
