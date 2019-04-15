import os
import time


print("Last modified: %s" % time.ctime(os.path.getmtime(r".\ex64.py")))
print("Created: %s" % time.ctime(os.path.getctime(r".\ex64.py")))
