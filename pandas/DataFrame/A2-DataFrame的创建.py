import pandas as pd
import numpy as np
from pandas import Series,DataFrame

#1、随机生成，需要输入data二维表数据  以及 行index 以及列 columns
data =DataFrame(data=np.random.randint(0,100,size=(3,5)),index=list('abc'),columns=list('ABCDE'))
'''
    A   B   C   D   E
a   2  83  60   8   7
b   1   7  43  72  32
c  58  46  47  73  20
'''

#使用字典的方式进行构造，字典中的各个key所对应的位置可以是浮点、整型等
dic = {
    'A':np.random.randint(0,100,size=3),
    'B':np.random.randint(0,100,size=3),
    'C':np.random.randint(0,100,size=3),
    'D':np.random.randint(0,100,size=3),
    'E':np.random.randint(0,100,size=3)
}

print(DataFrame(data=dic))



#从文件中进行读取
'''
pd.read_sql_table()
pd.read_csv
...

'''



#使用Series进行创建






【以下，当数据量过大的时候，可以使用pd读取文件的方式进行处理】
'''
做一个练习

根据以下考试成绩，创建一个DataFrame，命名为df
    张三 李四
语文 100   0
数学 70    100
英语 80    59
其它 90    89
'''


datas = [
[100 ,0],
 [70,100],
    [80,59],
    [90,89]
]
df  = DataFrame(data=datas,index=['语文','数学','英语','其它'],columns=['张三','李四'])
print(df)


