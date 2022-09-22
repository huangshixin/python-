import pandas as pd
import numpy as np
from pandas import Series,DataFrame

np.random.seed(100)
data  = np.random.randint(0,100,size=(4,5))
# print(data[:,[0,1,3]])


#如果想使用dataframe进行访问需要如何处理？

data2 = DataFrame(np.random.randint(0,100,size=(4,5)),columns=list('ABCDE'),index=list('abcd'))
print(data2)

#dataframe是一个按照列访问的字典 [访问的方式是  按照列 ，且列表中存在列表索引]
print(data2['D'])
print('\n',data2[['A','D']])
print(data2.loc[['a','b']])  #loc访问的是 显式索引，
print(data2.iloc[[0,1,3]])#代表隐式索引
'''
    A   B   C   D   E
a   9  93  86   2  27
b   4  31   1  13  83
c   4  91  59  67   7
d  49  47  65  61  14
   A   B   C   D   E
a  9  93  86   2  27
b  4  31   1  13  83
    A   B   C   D   E
a   9  93  86   2  27
b   4  31   1  13  83
d  49  47  65  61  14
'''


#按照数字的元素进行访问；

'''
loc  显式

iloc 隐式

df['a']

df[[需要查询的索引]]
'''



#【切片操作】
'''
    A   B   C   D   E
a   9  93  86   2  27
b   4  31   1  13  83
c   4  91  59  67   7
d  49  47  65  61  14
'''

'''
索引表示的是列索引


切片表示的是行切片


----------在dataframe中的索引都是 闭区间-----------
'''


#行切片
print(data2.loc['a':'c'])

#列切片 ----显式 and 隐式
print(data2.loc[:,'A':'B'])  #先保留行 再进行列的切片
print(data2.iloc[:,0:2])


#最常见的切片方式:

print(data2.loc0['a':'b','A':'B'])
https://www.bilibili.com/video/BV13P4y1f7db/?p=18&spm_id_from=pageDriver&vd_source=b498949199c494447b72f71d8016104d
