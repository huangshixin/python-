#计算期望和方差
'''
期望：E(x) = np
方差：Var(x) = np(1‐p)
利用stats.binom.stats(n, p, loc=0, moments='mv')计算期望和方差
moments参数中:m为期望，v为方差
'''
'''poisson.pmf(k) = exp(-lam) *lam**k / k!
原式子=（e的负lam次方 * lam的k次方）/k的阶乘


numpy代码中random模块的代码
numpy.random.poisson(lam=1.0, size=None) 

'''
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(20200605)
lam=42/6#平均值：平均每十分钟街道42、6次订票电话
size=50000
x=np.random.poisson(lam,size)
'''或者
#模拟服从泊松分布的50000个随机变量
x = stats.poisson.rvs(lam,size=size)
'''
print(np.sum(x==6)/size)

plt.hist(x,color='black')
plt.xlabel("随机变量：每十分钟接到订票电话的次数")
plt.ylabel("5000个样本中出现的次数")
plt.show()

# s = stats.binom.pmf(range(n + 1), n, p)
# print(np.around(s,3))
# # [0.25 0.5 0.25]
#用poisson.pmf(k, mu)求对应分布的概率:概率质量函数 (PMF)
x=stats.poisson.pmf(6,lam)
print(x)

