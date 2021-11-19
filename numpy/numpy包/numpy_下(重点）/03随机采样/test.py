import numpy as np

#生成一个列表 把1-100存入列表 逆序
list_1=[]
for i in range(100):
    list_1.insert(0,str(i+1))
print(list_1)

list_2=[]
for i in range(100):
    list_2.append(i+1)
list_2.sort(reverse=True)
print(list_2)

list_3=list(range(100,0,-1))
print(list_3)







