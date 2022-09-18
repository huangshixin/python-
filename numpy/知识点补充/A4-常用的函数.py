import numpy as np

1、np.ones()
2、np.zeros()
3 np.eye()生成对角线为1的数组或者矩阵
np.normal()生成正太分布
np.any()
np.all()
np.random.randn()随机的浮点数
np.random.randint()随机的整数
np.random.permutation()
np.random.linspace(stat,end,步长)
np.random.random()

几种属性类型：
ndim shape dtype size

数组的访问
arr[a][b] or arr[a,b]
arr[index1,index2,index3,...]


切片:
一维;
arr[::-1]
arr[1:]
arr[-2:]
二维
arr[:,:]
arr[:,1:]



聚合计算
np.sum
np.min
np.max
np.mean()求均值
np.median
np.argmax
np.argmin
np.std()标准差
np.var()协方差
np.any
np.all



广播运算
1、缺失维度补位
2、用已有的值填充
保证参于广播的两个数组能够达到同一个维度，如果达不到，就【无法广播】



排序
np.sort()#其中支持换 ’快排、堆排‘等
np.partition（）
