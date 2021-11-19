import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
'''
【例】模拟投硬币，投2次，请问两次都为正面的概率？
'''
np.random.seed(20200605)
n=2 #做某件事情的次数，这里是投两次硬币
p=0.5#做某件事情成功的概率，在这里即投硬币为正面的概率
size=50000
x=np.random.binomial(n,p,size)#这个方法的效果就是对二项分布进行采样
""" n 表示做了n此伯努利实验 size表示采样的次数，p就是概率"""

print(np.sum(x==0)/size)# 0.25154
print(np.sum(x==1)/size)# 0.49874
print(np.sum(x==2)/size)# 0.24972

plt.hist(x,color='green',density=True)#控制柱子的颜色和值
print(plt.hist(x,density=True))
# array([1.2577, 0.    , 0.    , 0.    , 0.    , 2.4937, 0.    , 0.    ,
#        0.    , 1.2486]), \柱子的值
# array([0. , 0.2, 0.4, 0.6, 0.8, 1. , 1.2, 1.4, 1.6, 1.8, 2. ])
plt.xlabel('随机变量：硬币为正面的次数')
plt.ylabel('50000个样本中出现的次数')
plt.show()
#它返回一个列表，列表中每个元素表示随机变量中对应值的概率
s = stats.binom.pmf(range(n + 1), n, p)
print(np.around(s,3))
# [0.25 0.5 0.25]




























