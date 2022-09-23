import pandas as pd
import numpy as np
from pandas import Series,DataFrame

'''
有两种丢失数据：
1、None
2、np.nan(NaN)  

[tips]
NaN不能用于计算，它只是用于展示， np.nan是浮点型；
np.nan与任何数进行计算，结果都为None
'''
A = np.nan
A1 = DataFrame(data=np.random.randint(0,10,size=(3,4)),index=list('ABC'),columns=list('abcd'))
print(A)
print(A1)
A1.loc['A','b']=np.nan
print(A1,A1.dtypes)
'''
   a  b  c  d
A  1  8  2  8
B  3  7  4  0
C  4  6  2  1
   a    b  c  d
A  1  NaN  2  8
B  3  7.0  4  0
C  4  6.0  2  1

查看类型
a      int32
b    float64
c      int32
d      int32
dtype: object
'''



#新的操作【空值的操作】
'''
isnull
notnull
dropna()丢掉
fillna()填充
'''
np.random.seed(100)
A2 = DataFrame(data=np.random.randint(0,20,size=(4,5)),index=list('abcd'),columns=list('ABCDE'))
A2.loc['a':'c','B':'E']=np.nan
'''

print(A2)
    A    B     C    D     E
a  16  NaN   NaN  NaN   NaN
b  17  NaN   NaN  NaN   NaN
c   7  NaN   NaN  NaN   NaN
d  11  0.0  18.0  9.0  10.0
'''
print(A2.isnull(),'\n',A2.notnull()) #这是一对相反的
print(A2.isnull().any(axis=0))#默认是列方向 0 是按照行方向查 ，相当于查找列
print(A2.isnull().any(axis=1))

#对一个二维表格而言， 【行方向是【字段】】，【列方向是数据】
A2.iloc[0,0]=np.nan
'''
      A     B    C    D     E
a   NaN   NaN  NaN  NaN   NaN
b  10.0   NaN  NaN  NaN   NaN
c   2.0   NaN  NaN  NaN   NaN
d  11.0  16.0  9.0  2.0  12.0

上述可以理解为
dic = {
'a' = [NaN   NaN  NaN  NaN   NaN],
'b' = [10.0   NaN  NaN  NaN   NaN]
...

}
'''
#dropna按照行进行删除，只要数据有NaN就把整个的数据清空【因为行的索引是一个key，对应的行方向的延申是一个数据 'b' = [10.0   NaN  NaN  NaN   NaN]
print(A2.dropna())

#填充

print(A2.fillna(value=A2.mean(axis=0)))
'''
           A     B    C    D     E
a   7.666667  16.0  9.0  2.0  12.0
b  10.000000  16.0  9.0  2.0  12.0
c   2.000000  16.0  9.0  2.0  12.0
d  11.000000  16.0  9.0  2.0  12.0

'''
'''
backfill bfill 向后填充
pad ffill向前填充
'''
print(A2.fillna(axis=1,method='ffill'))
'''
      A     B     C     D     E
a   NaN   NaN   NaN   NaN   NaN
b  10.0  10.0  10.0  10.0  10.0
c   2.0   2.0   2.0   2.0   2.0
d  11.0  16.0   9.0   2.0  12.0
'''
