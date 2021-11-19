#numpy.random.uniform(low=0.0, high=1.0, size=None)

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

"""
numpy.random.uniform(low=0.0, high=1.0, size=None)

"""
np.random.seed(20200614)
a = 0
b = 100
size = 50000
x = np.random.uniform(a, b, size=size)
print(np.all(x >= 0)) # True
print(np.all(x < 100)) # True
y = (np.sum(x<50)-np.sum(x<10))/size
print(y) # 0.40144
plt.hist(x, bins=20)
plt.show()
a = stats.uniform.cdf(10, 0, 100)
b = stats.uniform.cdf(50, 0, 100)
print(b - a) # 0.4


#例子
np.random.seed(20200614)
print(np.random.rand())
# 0.7594819171852776
print(np.random.rand(5))
# [0.75165827 0.16552651 0.0538581 0.46671446 0.89076925]
print(np.random.rand(4, 3))
# [[0.10073292 0.14624784 0.40273923]
# [0.21844459 0.22226682 0.37246217]
# [0.50334257 0.01714939 0.47780388]
# [0.08755349 0.86500477 0.70566398]]
np.random.seed(20200614)
print(np.random.uniform()) # 0.7594819171852776
print(np.random.uniform(size=5))
# [0.75165827 0.16552651 0.0538581 0.46671446 0.89076925]
print(np.random.uniform(size=(4, 3)))
# [[0.10073292 0.14624784 0.40273923]
# [0.21844459 0.22226682 0.37246217]
# [0.50334257 0.01714939 0.47780388]
# [0.08755349 0.86500477 0.70566398]]


'''【例】若 high 不为 None 时，取[low,high)之间随机整数，否则取值[0,low)之间随机整数。'''

np.random.seed(20200614)
x = np.random.randint(2, size=10)
print(x)
# [0 0 0 1 0 1 0 0 0 0]
x = np.random.randint(1, size=10)
print(x)
# [0 0 0 0 0 0 0 0 0 0]
x = np.random.randint(5, size=(2, 4))
print(x)
# [[3 3 0 1]
# [1 1 0 1]]
x = np.random.randint(1, 10, [3, 4])
print(x)
# [[2 1 7 7]
# [7 2 4 6]
# [8 7 2 8]]
