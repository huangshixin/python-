import  numpy as np

#对一维数组进行切片
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(x[0:2])#numpy 和python一样只能左闭右开
print(x[1:5:2])#stride =2
print(x[-2:])#  [7 8] 代表从倒三开始输出到最后
print(x[:-2])#[1 2 3 4 5 6]
print(x[:])#打印全部
print(x[::-1])# [8 7 6 5 4 3 2 1] 最外边的-1是步长 但是这种写法相当于逆序


#对二维切片
x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
"二维数组，可以看作是列表当中存放着列表" \
"所以打印方式和一维列表一样"
print(x[0:2])#对与array而言，本身也是一个列表当中存放的咧白哦
print(x[-1])
print(x[:-2])
print(x[:])
print(x[:2])



'''

思考一个问题，如果我们获得一个数据集 ，数据集是表格的形式 那我们是不是可以使用这种切片的方式来取值呢？
print(x[:,:-2] 代表每一行我都要 但是最后一列不要
print(x[1:,:-2] 代表第一行不要  最后一列不要
'''
"以下，我们可以认为x[横坐标，纵坐标]的取值"
print(x[0,1:4])#[12 13 14]
print(x[1:4,0])
print(x[1:3, 2:4])
print(x[:, :])
print(x[::2, ::2])
"#整个矩阵 按照行逆序输出"
print(x[::-1, :])
"#整个矩阵 按照列 逆序输出"
print(x[:, ::-1])


"dots索引"
# NumPy 允许使用 ... 表示足够多的冒号来构建完整的索引列表。
# 比如，如果 x 是 5 维数组：
# 1. x[1,2,...] 等于 x[1,2,:,:,:] 2. x[...,3] 等于 x[:,:,:,:,3] 3. x[4,...,5,:] 等于 x[4,:,:,5,:]

x=np.random.randint(1,100,[2,2,3])
print(x)
print(x[1, ...])
print(x[1, ...])


"整数数组索引"
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
r = [0, 1, 2]
print(x[r])
x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])

print(x[r])

#布尔索引
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y =x>5
"以下是判断false 和true"
print(y)# [False False False False False  True  True  True]
"以下输出列表"
print(x[x>5])
x = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
y = np.logical_not(np.isnan(x))
print(x[y])


import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,50)
y=np.sin(x)
print(len(x))
plt.plot(x,y)
mask = y >=0
print(len(x[mask]))
print(mask)

#数组迭代
"除了for循环，NUMpy还提供了一种更为优雅的遍历方法"
"求某一列或者某一行的和"
x= np.array([[11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25],
             [26, 27, 28, 29, 30],
             [31, 32, 33, 34, 35]])
"当axis" \
" 是0的时候 是列 " \
"是 1的时候  是行"
y=np.apply_along_axis(np.sum,0,x)
print(y)
y=np.apply_along_axis(np.sum,1,x)
print(y)
"np.mean  求均值"
y=np.apply_along_axis(np.mean,0,x)
print(y)
y=np.apply_along_axis(np.mean,1,x)
print(y)


'''
np.ndim(x)看你是哪一种维度的   比如二维数组
type（x）看你的类型 
dtype(x)看 属性
mean求均值
sum求和
argmax返回最大值的角标index
argmin 返回最小值的角标
nonzero返回非0的角标
'''






