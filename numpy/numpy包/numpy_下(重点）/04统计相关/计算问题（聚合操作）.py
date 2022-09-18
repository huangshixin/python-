import numpy as np



'''计算最小值'''
x = np.array([
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])
'''最小值函数：min'''

#python自带 x.min()  或者 x = min(x)
#numpy中 np.min(x)
value=np.min(x)
print(value)

print('打印列上的最小值(用min函数)：\n',np.min(x,axis=0))
print('打印行上的最小值：\n',np.min(x,axis=1))
print('Mininum value was printed on the computer（用min函数）:\n',np.min(x,axis=0))
print('全局最小,并使用min判断\n',np.min(x))
lists=[2,4,56,7,8,0,5,8,5,7]
print('python自带的min这种方法，只能去识别列表',min(lists))
'''
    min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value
'''
print('###############################################################################')


'''计算最大值'''
#axis 还是遵守 0 行 1 列 【例如：你现在给定一个二维数组，你需要从找到每一行的最大值，你可以设置axis=0，系统会去逐行寻找最大值，并输出】
y = np.max(x)
print(y) # 35
y = np.max(x, axis=0)
print(y) # [31 32 33 34 35]
y = np.max(x, axis=1)
print(y) # [15 20 25 30 35]
'''同理 还有np.max()'''






'''计算极差
极差，又称范围误差或全距，用字母R表示，是用来表示统计资料中的变异量数，
通过最大值减最小值后得出数据，通常用来反映一组数据变化范围的大小。极差
不能用作比较，因为数据的单位不同，方差能用作比较，因为都是个比率。
'''
print('\n计算极差###########################################################\n')
np.random.seed(20200623)
x = np.random.randint(0, 20, size=[4, 5]) #这里是[] or ()都可以
print(x)
# [[10 2 1 1 16]
# [18 11 10 14 10]
# [11 1 9 18 8]
# [16 2 0 15 16]]
print(np.ptp(x)) # 18
print(np.ptp(x, axis=0)) # [ 8 10 10 17 8]
print(np.ptp(x, axis=1)) # [15 8 17 16]




'''计算分位数
q：介于0-100的float，用来计算是几分位的参数，如四分之一位就是25，如要算两个位置
的数就[25,75]。

'''
print('\n计算分位数########################################################\n')
np.random.seed(20200623)
x = np.random.randint(0, 20, size=[4, 5])

# [[10 2 1 1 16]
# [18 11 10 14 10]
# [11 1 9 18 8]
# [16 2 0 15 16]]
print(sum(x))
print(np.percentile(x, [25, 50]))#相当于计算 1/4  1/2
# [ 2. 10.]
print(np.percentile(x, [25, 50], axis=0))
# [[10.75 1.75 0.75 10.75 9.5 ]
# [13.5 2. 5. 14.5 13. ]]
print(np.percentile(x, [25, 50], axis=1))
# [[ 1. 10. 8. 2.]
# [ 2. 11. 9. 15.]]



'''计算中位数'''

np.random.seed(20200623)
x = np.random.randint(0, 20, size=[4, 5])
print(x)
# [[10 2 1 1 16]
# [18 11 10 14 10]
# [11 1 9 18 8]
# [16 2 0 15 16]]

print(np.percentile(x, 50))
print(np.median(x))
# 10.0
print(np.percentile(x, 50, axis=0))
print(np.median(x, axis=0))
# [13.5 2. 5. 14.5 13. ]
print(np.percentile(x, 50, axis=1))
print(np.median(x, axis=1))
# [ 2. 11. 9. 15.]






'''计算平均值 mean
numpy.mean(a[, axis=None, dtype=None, out=None, keepdims=np._NoValue)]) 
'''
print('\n计算平均值 mean#########################################################\n')
x = np.array([
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])
y=np.mean(x)
print('打印数组的均值:',y)

print('打印列均值',np.mean(x,axis=0))
print('打印行均值',np.mean(x,axis=1))




'''计算加权平均值 average'''
print('\n计算加权平均值 average###########################################################################################\n')
x = np.array([
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])

y = np.average(x)
print(y) # 23.0
y = np.average(x, axis=0)
print(y) # [21. 22. 23. 24. 25.]
y = np.average(x, axis=1)
print(y) # [13. 18. 23. 28. 33.]
y = np.arange(1, 26).reshape([5, 5])
print(y)
# [[ 1 2 3 4 5]
# [ 6 7 8 9 10]
# [11 12 13 14 15]
# [16 17 18 19 20]
# [21 22 23 24 25]]
z = np.average(x, weights=y)
print(z) # 27.0
z = np.average(x, axis=0, weights=y)
print(z)
# [25.54545455 26.16666667 26.84615385 27.57142857 28.33333333]
z = np.average(x, axis=1, weights=y)
print(z)
# [13.66666667 18.25 23.15384615 28.11111111 33.08695652]




'''计算方差'''
'''
numpy.var(a[, axis=None, dtype=None, out=None, ddof=0, keepdims=np._NoValue])
'''
x = np.array([
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])

y = np.var(x)
print(y) # 52.0
y = np.mean((x - np.mean(x)) ** 2)
print(y) # 52.0

y = np.var(x, ddof=1)
print(y) # 54.166666666666664
y = np.sum((x - np.mean(x)) ** 2) / (x.size - 1)
print(y) # 54.166666666666664
y = np.var(x, axis=0)
print(y) # [50. 50. 50. 50. 50.]
y = np.var(x, axis=1)
print(y) # [2. 2. 2. 2. 2.]





'''计算协方差矩阵'''
x = [1, 2, 3, 4, 6]
y = [0, 2, 5, 6, 7]
print(np.cov(x)) # 3.7 #样本方差
print(np.cov(y)) # 8.5 #样本方差
print(np.cov(x, y))
# [[3.7 5.25]
# [5.25 8.5 ]]
print(np.var(x)) # 2.96 #方差
print(np.var(x, ddof=1)) # 3.7 #样本方差
print(np.var(y)) # 6.8 #方差
print(np.var(y, ddof=1)) # 8.5 #样本方差
z = np.mean((x - np.mean(x)) * (y - np.mean(y))) #协方差
print(z) # 4.2
z = np.sum((x - np.mean(x)) * (y - np.mean(y))) / (len(x) - 1) #样本协方差
print(z) # 5.25
z = np.dot(x - np.mean(x), y - np.mean(y)) / (len(x) - 1) #样本协方差
print(z) # 5.25





'''相关系数'''
#numpy.corrcoef(x, y=None, rowvar=True, bias=np._NoValue, ddof=np._NoValue)
x, y = np.random.randint(0, 20, size=(2, 4))
print(x) # [10 2 1 1]
print(y) # [16 18 11 10]
z = np.corrcoef(x, y)
print(z)
# [[1. 0.48510096]
# [0.48510096 1. ]]
a = np.dot(x - np.mean(x), y - np.mean(y))
b = np.sqrt(np.dot(x - np.mean(x), x - np.mean(x)))
c = np.sqrt(np.dot(y - np.mean(y), y - np.mean(y)))
print(a / (b * c)) # 0.4851009629263671




'''直方图'''
'''
numpy.digitize(x, bins, right=False) Return the indices of the bins to which each value
in input array belongs.
x：numpy数组
bins：一维单调数组，必须是升序或者降序
right：间隔是否包含最右
返回值：x在bins中的位置
'''
x = np.array([0.2, 6.4, 3.0, 1.6])
bins = np.array([0.0, 1.0, 2.5, 4.0, 10.0])
inds = np.digitize(x, bins)
print(inds) # [1 4 3 2]
for n in range(x.size):
    print(bins[inds[n] - 1], "<=", x[n], "<", bins[inds[n]])
# 0.0 <= 0.2 < 1.0
# 4.0 <= 6.4 < 10.0
# 2.5 <= 3.0 < 4.0
# 1.0 <= 1.6 < 2.5
x = np.array([1.2, 10.0, 12.4, 15.5, 20.])
bins = np.array([0, 5, 10, 15, 20])
inds = np.digitize(x, bins, right=True)
print(inds) # [1 2 3 4 4]
inds = np.digitize(x, bins, right=False)
print(inds) # [1 3 3 4 5]

























