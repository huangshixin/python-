import pandas as pd
import numpy as np
from pandas import Series,DataFrame

arr =np.ones((4,5))
#print(arr)
'''
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
 
'''


'''
0行1列的【解释】

0 表示的是按照行的【orientation】进行求和
同理 1表示按照列的方向进行求和
'''
print(arr.sum(axis=0))

'''
[4. 4. 4. 4. 4.]
'''






#dataframe
data = pd.DataFrame(data=arr)
'''

'''
print(data.mean(axis=0))

#查看values
print(data.values)
#求median()

#求sum


#求和----维度一致
np.random.seed(10)
data1 = pd.DataFrame(np.random.randint(0,10,size=(3,4)))
data2 = pd.DataFrame(np.random.randint(0,100,size=(3,4)))
print(data1+data2)

#numpy和dataframe之间的运算
data3 = np.random.randint(0,10,size=4)
print('data1\n',data1)
print('data3\n',data3)
'''
data1
    0  1  2  3
0  9  4  0  1
1  9  0  1  8
2  9  0  8  6
data3
 [[5 3 9 6]
 [9 1 9 4]
 [2 6 7 8]]
'''
print(data1+data3) #对应位置相加
'''
    0  1   2   3
0  14  7   9   7
1  18  1  10  12
2  11  6  15  14
'''

