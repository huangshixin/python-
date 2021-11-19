import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from numpy import  random as rd


'''
当x>0时，f（x）=lam*exp（-lam*x）
当x<=0时，f(x）=0
numpy.random.exponential(scale=1.0, size=None)
'''

#【例】 scale = 1/lambda

rd.seed(20202)
lam=7
size=50000
x=np.random.exponential(1/lam,size)
y1 = (np.sum(x < 1 / 7)) / size
y2 = (np.sum(x < 2 / 7)) / size
y3 = (np.sum(x < 3 / 7)) / size
print(y1) # 0.63218
print(y2) # 0.86518
print(y3) # 0.95056
plt.hist(x, bins=20)
plt.show()


y1 = stats.expon.cdf(1 / 7, scale=1 / lam)
y2 = stats.expon.cdf(2 / 7, scale=1 / lam)
y3 = stats.expon.cdf(3 / 7, scale=1 / lam)
print(y1) # 0.6321205588285577
print(y2) # 0.8646647167633873
print(y3) # 0.950212931632136


#随机函数
'''
numpy.random.choice(a, size=None, replace=True, p=None)
从序列中获取元素，若 a 为整数，元素取值从 np.range(a) 中随机获取；若 a 为数组，取值从 a 数组
元素中随机获取。该函数还可以控制生成数组中的元素是否重复 replace ，以及选取元素的概率 p 。
'''
np.random.seed(20200614)
x = np.random.choice(10, 3)
print(x) # [2 0 1]
x = np.random.choice(10, 3, p=[0.05, 0, 0.05, 0.9, 0, 0, 0, 0, 0, 0])
print(x) # [3 2 3]
x = np.random.choice(10, 3, replace=False, p=[0.05, 0, 0.05, 0.9, 0, 0, 0, 0, 0, 0])
print(x) # [3 0 2]
aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
x = np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3])
print(x) # ['pooh' 'rabbit' 'pooh' 'pooh' 'pooh']
np.random.seed(20200614)
x = np.random.randint(0, 10, 3)
print(x) # [


'''
对数据集进行洗牌操作
numpy.random.shuffle(x) 
对 x 进行重排序，如果 x 为多维数组，只沿第 0 轴洗牌，改变原来的数组，输出为None。


数据一般都是按照采集顺序排列的，但是在机器学习中很多算法要求数据之间相互独立，所以需要对数据集进行洗牌操作
'''
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
np.random.seed(20200614)
x = np.arange(10)
np.random.shuffle(x)
print(x)


print(rd.shuffle([1,2,9,12,15]))

x=np.arange(20).reshape((5,4))
print(x)


print("洗牌操作")
rd.seed(2320)
rd.shuffle(x)#洗牌时不返回值的
print(x)
