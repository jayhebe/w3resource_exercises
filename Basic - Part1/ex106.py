import os


path_list = ['test.txt', 'filename', '/user/system/test.txt', '/', '']
for p in path_list:
    print('"%s" :' % p, os.path.splitext(p))
