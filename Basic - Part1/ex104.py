import os


print("Effective group id: ", os.getegid())
print("Effective user id: ", os.geteuid())
print("Real group id: ", os.getgid())
print("List of supplemental group ids: ", os.getgroups())
