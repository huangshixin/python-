#练习1
#【思考Serise和ndarray的运算规则有什么不同？
#新建另一个索引包含‘文综；的Series s2，并与s2进行多种算术计算
import pandas as pd
import numpy as np
from pandas import Series
'''
Series和numpy运算的区别是：
Serise支持【索引对其】
numpy支持【广播】
'''

index1 = ['语文','数学','英语','文综']
index2 = ['语文','数学','英语','理综']
np.random.seed(10)
S1 = Series(data=np.random.randint(60,150,size=4),index=index1,name='文科')
S2 = Series(data=np.random.randint(60,150,size=4),index=index2,name='理科')
print(S1,'\n',S2)



#1、随机生成两组学生成绩
np.random.seed(1)
indexStu = ['lucy','mery','tom','jack']
stuPython = Series(data=np.random.randint(10,100,size=4),index=indexStu)
stuJave = Series(data=np.random.randint(10,100,size=4),index=indexStu)

#计算每个学生的平均值  ---Mean
sums = stuPython+stuJave
print('平均成绩={}\n'.format(sums/2)) #支持列表直接除




#找出python中几个不及格的学生的姓名：
unscore = [stuPython<60]#先拿到True False索引
print(stuPython)
print(stuPython.index[unscore])



#需要给mery的python成绩加上10分

if stuPython.loc['mery']<90:
    stuPython.loc['mery']+=10
else:
    stuPython['mery']=100
print(stuPython.loc['mery'])


#计算各个学科的班级的平均成绩
MeanPython = np.mean(stuPython)
print(f'Python平均值 ='+str(MeanPython),'Java平均值={}'.format(np.mean(stuJave)))
