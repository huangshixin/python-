#在超几何分布中，各次实验不是独立的，各次实验成功的概率也不等。 超几何分布概率函数的数学表
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
p(k,M,n,N)= (n,k)*(M-n, N-k)/(M,N)
(n,k):表示从k个中选取出n个
以此类推


numpy.random.hypergeometric(ngood, nbad, nsample, size=None) 
表示对一个超几何分布进行采样， size 表示采样的次数， ngood 表示总体中具有成功标志的元素个
数， nbad 表示总体中不具有成功标志的元素个数， ngood+nbad 表示总体样本容量， nsample 表示抽
取元素的次数（小于或等于总体样本容量），函数的返回值表示抽取 nsample 个元素中具有成功标识
的元素个数
"""
np.random.seed(20200605)
size = 500000
x = np.random.hypergeometric(ngood=7, nbad=13, nsample=12, size=size)
'''或者
#用rvs(M, n, N, loc=0, size=1, random_state=None)模拟
x = stats.hypergeom.rvs(M=20,n=7,N=12,size=size)
'''
print(np.sum(x == 3) / size) # 0.198664
plt.hist(x, bins=8)
plt.xlabel('狗的数量')
plt.ylabel('50000个样本中出现的次数')
plt.title('超几何分布',fontsize=20)
plt.show()
"""
M 为总体容量
n 为总体中具有成功标志的元素的个数
N,k 表示抽取N个元素有k个是成功元素
"""
x = range(8)
#用hypergeom.pmf(k, M, n, N, loc)来计算k次成功的概率
s = stats.hypergeom.pmf(k=x, M=20, n=7, N=12)
print(np.round(s, 3))
# [0. 0.004 0.048 0.199 0.358 0.286 0.095 0.01 ]
'''
超几何分布的均值与方差
均值E(x) = N(n/M)
方差Var(x) = N(n/M)(1‐n/M)((M‐N)/(M‐1))
注释：考虑n次实验的超几何分布，令p=n/M,当总体容量足够大时((M‐N)/(M‐1))近似于1，此时数学期望为
Np，方差为Np(1‐p).
#用stats(M, n, N, loc=0, moments='mv')计算均值和方差
stats.hypergeom.stats(20,7,12,moments='mv')
'''



