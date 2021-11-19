import numpy as  np
import matplotlib.pyplot as plt
from  scipy import  stats

"""
野外正在进行9（n=9）口石油勘探井的发掘工作，每一口井能够开发出油的概率是
0.1（p=0.1）。请问，最终所有的勘探井都勘探失败的概率？
(1-0.1)^9  就是二项分布
"""

np.random.seed(20200605)
n = 9# 做某件事情的次数
p = 0.1# 做某件事情成功的概率
size=50000
x=np.random.binomial(n,p,size)#二项分布
'''或者使用binom.rvs
#使用binom.rvs(n, p, size=1)函数模拟一个二项随机变量,可视化地表现概率
y = stats.binom.rvs(n, p, size=size)#返回一个numpy.ndarray
'''
print(np.sum(x==0)/size)# 0.3897

plt.hist(x)
plt.xlabel('随机变量：成功次数')
plt.ylabel('样本中出现的次数')
plt.show()
#它返回一个列表，列表中每个元素表示随机变量中对应值的概率
s = stats.binom.pmf(range(10), n, p)
print(np.around(s,3))
# [0.387 0.387 0.172 0.045 0.007 0.001 0. 0. 0. 0. ]



