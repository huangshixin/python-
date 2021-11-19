import numpy as np
import json
import os

paths=os.getcwd()#获得当前文件所在的绝对路径
# absolute_path=os.path.abspath()
file_path=paths+r'.\new_test.txt'
print(file_path)
filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
with open(file_path,'r+') as files:
    print("File information will print on the computer")
    print(files.read())
    print("xxxxxx")
    for i in range(len(filenames)):
        print(i)
        files.write(filenames[i])
    print("sdfasfasdasasd")
    print(files.read())
#