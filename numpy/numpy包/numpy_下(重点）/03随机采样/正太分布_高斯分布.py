#正太分布

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
f(x)=exp(-x**2/2)/sqrt(2*np.pi)
numpy.random.randn(d0, d1, ..., dn)

Return a sample (or samples) from the "standard
normal" distribution
根据指定大小产生满足标准正态分布的数组（均值为0，标准差为1）。
"""
np.random.seed(20200614)
size = 50000
x = np.random.randn(size)#从正太分布的采样当中返回数
y1 = (np.sum(x < 1) - np.sum(x < -1)) / size
y2 = (np.sum(x < 2) - np.sum(x < -2)) / size
y3 = (np.sum(x<3) - np.sum(x < -3)) / size
print(y1) # 0.68596
print(y2) # 0.95456
print(y3) # 0.99744

plt.hist(x, bins=20)
plt.show()

y1 = stats.norm.cdf(1) - stats.norm.cdf(-1)
y2 = stats.norm.cdf(2) - stats.norm.cdf(-2)
y3 = stats.norm.cdf(3) - stats.norm.cdf(-3)
print(y1) # 0.6826894921370859
print(y2) # 0.9544997361036416
print(y3)


#18
np.random.seed(20200614)
x = 0.5 * np.random.randn(2, 4) + 5
'''或者
#模拟10000个随机变量
x = 0.5*stats.norm.rvs(size=(2,4))+5
'''
print(x)
# [[5.39654234 5.4088702 5.49104652 4.95817289]
# [4.31977933 4.76502391 4.70720327 4.36239023]]
np.random.seed(20200614)
mu = 5#平均值
sigma = 0.5#标准差
x = np.random.normal(mu, sigma, (2, 4))
print(x)
# [[5.39654234 5.4088702 5.49104652 4.95817289]
# [4.31977933 4.76502391 4.70720327 4.36239023]]
size = 50000
x = np.random.normal(mu, sigma, size)
print(np.mean(x)) # 4.996403463175092
print(np.std(x, ddof=1)) # 0.4986846716715106（#样本标准差）
'''
ddof：int, optional
Means Delta Degrees of Freedom. The divisor used in calculations is N ‐ ddof, where N
represents the number of elements. By default ddof is zero.
'''
plt.hist(x, bins=20)#生成柱状图
plt.show()




'''
from numpy import random as rd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as  sns
#生成大小2x3 随机正太分布
x=rd.normal(size=(2,3))
print(x)

#生成大小为2x3的随机正态分布，平均值为1，标准差为2
y=rd.normal(loc=1,scale=2,size=(2,3))
print(y)
sns.distplot(rd.normal(size=1000), hist=True)#hist这是生成柱状图的效果
#displot是曲线图
plt.show()

'''