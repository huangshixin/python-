import numpy as np

#排序
# 1. numpy.sort(a[, axis=-1, kind='quicksort', order=None]) Return a sorted copy of an array.
# a. axis：排序沿数组的（轴）方向，0表示按行，1表示按列，None表示展开来排序，默认为-1，表示沿最后的轴排序。
# b. kind：排序的算法，提供了快排'quicksort'、混排'mergesort'、堆排'heapsort'， 默认为‘quicksort'。
# c. order：排序的字段名，可指定字段排序，默认为None。
"""
在机器学习和深度学习中我们常见到np.random.seed()利用随机数种子，使得每次生成的随机数相同。
numpy.randn.randn(d0，d1，...，dn)
randn函数根据给定维度生成大概率在（-2.58~+2.58）之间的数据
randn函数返回一个或者一组样本，具有标准正态分布
dn表示每个维度
返回值为指定维度的array
"""
"""if __name__ == '__main__'
相当于指定某个模块先执行
"""
np.random.seed(20200612)
# print(np.random.seed(20200612))
x = np.random.rand(5, 5) * 10
x = np.around(x, 2)
print(x)
y = np.sort(x)
print(y)
y=np.sort(x,axis=0)
print(y)
y=np.sort(x,axis=1)
print(y)
dt = np.dtype([('name', 'S10'), ('age', np.int)])
a = np.array([("Mike", 21), ("Nancy", 25), ("Bob", 17), ("Jane", 27)], dtype=dt)
b = np.sort(a, order='name')
print(b)
# [(b'Bob', 17) (b'Jane', 27) (b'Mike', 21) (b'Nancy', 25)]
b = np.sort(a, order='age')
print(b)
# [(b'Bob', 17) (b'Mike', 21) (b'Nancy', 25) (b'Jane', 27)]

np.random.seed(20200612)
x = np.random.randint(0, 10, 10)
print(x)
# [6 1 8 5 5 4 1 2 9 1]
y = np.argsort(x)
print(y)
# [1 6 9 7 5 3 4 0 2 8]
print(x[y])
# [1 1 1 2 4 5 5 6 8 9]
y = np.argsort(-x)
print(y)
# [8 2 0 3 4 5 7 1 6 9]
print(x[y])
# [9 8 6 5 5 4 2 1 1 1]


"""
 numpy.lexsort(keys[, axis=-1])
 给定多个可以在电子表格中解释为列的排序键，lexsort返回一个整数索引数组，该数组描述了按多个列排序的顺序。序列中的最后一个键
用于主排序顺序，倒数第二个键用于辅助排序顺序，依此类推。keys参数必须是可以转换为相同形状的数组的对象序列。如果为keys参数
提供了2D数组，则将其行解释为排序键，并根据最后一行，倒数第二行等进行排序。
"""
index=np.lexsort([x[:, 0]])
print(index)

x = np.array([1, 5, 1, 4, 3, 4, 4])
y = np.array([9, 4, 0, 4, 0, 2, 1])
a = np.lexsort([x])
b = np.lexsort([y])
print(a)
# [0 2 4 3 5 6 1]
print(x[a])
# [1 1 3 4 4 4 5]
print(b)
# [2 4 6 5 1 3 0]
print(y[b])
# [0 0 1 2 4 4 9]
z = np.lexsort([y, x])
print(z)
# [2 0 4 6 5 3 1]
print(x[z])
# [1 1 3 4 4 4 5]
z = np.lexsort([x, y])
print(z)
# [2 4 6 5 3 1 0]
print(y[z])
# [0 0 1 2 4 4 9]




np.random.seed(100)
x = np.random.randint(1, 30, [8, 3])
print(x)
# [[ 9 25 4]
# [ 8 24 16]
# [17 11 21]
# [ 3 22 3]
# [ 3 15 3]
# [18 17 25]
# [16 5 12]
# [29 27 17]]
y = np.sort(x, axis=0)
print(y)
# [[ 3 5 3]
# [ 3 11 3]
# [ 8 15 4]
# [ 9 17 12]
# [16 22 16]
# [17 24 17]
# [18 25 21]
# [29 27 25]]
z = np.partition(x, kth=2, axis=0)
print(z)
# [[ 3 5 3]
# [ 3 11 3]
# [ 8 15 4]
# [ 9 22 21]
# [17 24 16]
# [18 17 25]
# [16 25 12]
# [29 27 17]]


"""
np.linspace(start,end,num)等差
"""







"""
np.random.normal(loc, scale, size)
loc：float

此概率分布的均值（对应着整个分布的中心centre）

scale：float

此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）

size：int or tuple of ints

输出的shape，默认为None，只输出一个值
"""




"""
np.random.uniform(low, high, size)
    low: 采样下界，float类型，默认值为0；

    high: 采样上界，float类型，默认值为1；

    size: 输出样本数目，为int或元组(tuple)类型
"""
data=np.random.uniform(1,2,(3,2))
print(data)



"""
np.random


randint

random_integers

random_sample

random

rand
"""












"""
numpy.random.RandomState()

伪随机数产生器的种子

对于某一个伪随机数发生器，只要该种子（seed）相同，产生的随机数序列就是相同的
"""




"""
搜索
numpy.argmax(a[, axis=None, out=None])
softmax中会使用到这个函数


argmax返回的是最大数的索引.（返回一个角标）

argmax有一个参数axis,
默认是0,表示第几维的最大值
"""
np.random.seed(20200612)
x = np.random.rand(5, 5) * 10
x = np.around(x, 2)
print(x)
# [[2.32 7.54 9.78 1.73 6.22]
# [6.93 5.17 9.28 9.76 8.25]
# [0.01 4.23 0.19 1.73 9.27]
# [7.99 4.97 0.88 7.32 4.29]
# [9.05 0.07 8.95 7.9 6.99]]
y = np.argmax(x)
print(y) # 2
"""二维当中"""
y = np.argmax(x, axis=0)#表示的是列的看，第几列中的最大值的角标
print(y)
# [4 0 0 1 2]
y = np.argmax(x, axis=1)#表示的是行的看，第几列中的最大值的角标
print(y)
# [2 3 4 0 0]




"""三维当中"""
import numpy as np
a = np.array([
              [
                  [1, 5, 5, 2],
                  [9, -6, 2, 8],
                  [-3, 7, -9, 1]
              ],

              [
                  [-1, 5, -5, 2],
                  [9, 6, 2, 8],
                  [3, 7, 9, 1]
              ]
            ])
print(np.argmax(a, axis=0))
# [[0 0 0 0]
#      [0 1 0 0]
#      [1 0 1 0]]



"""
numppy.nonzero(a)

1. 只有 a 中非零元素才会有索引值，那些零值元素没有索引值。
2. 返回一个长度为 a.ndim 的元组（tuple），元组的每个元素都是一个整数数组（array）。
3. 每一个array均是从一个维度上来描述其索引值。比如，如果 a 是一个二维数组，则tuple包含两个array，第一个array从行维度来描述索引
值；第二个array从列维度来描述索引值。
4. 该 np.transpose(np.nonzero(x)) 函数能够描述出每一个非零元素在不同维度的索引值。
5. 通过 a[nonzero(a)] 得到所有 a 中的非零值。
"""

x = np.array([0, 2, 3])
print(x) # [0 2 3]
print(x.shape) # (3,)
print(x.ndim) # 1
y = np.nonzero(x)
print(y) # (array([1, 2], dtype=int64),)
print(np.array(y)) # [[1 2]]
print(np.array(y).shape) # (1, 2)
print(np.array(y).ndim) # 2
print(np.transpose(y))
# [[1]
# [2]]
print(x[np.nonzero(x)])
#[2, 3]
x = np.array([[3, 0, 0], [0, 4, 0], [5, 6, 0]])
print(x)
# [[3 0 0]
# [0 4 0]
# [5 6 0]]
print(x.shape) # (3, 3)
print(x.ndim) # 2
y = np.nonzero(x)
print(y)
# (array([0, 1, 2, 2], dtype=int64), array([0, 1, 0, 1], dtype=int64))
print(np.array(y))
# [[0 1 2 2]
# [0 1 0 1]]
print(np.array(y).shape) # (2, 4)
print(np.array(y).ndim) # 2
y = x[np.nonzero(x)]
print(y) # [3 4 5 6]
y = np.transpose(np.nonzero(x))
print(y)
# [[0 0]
# [1 1]
# [2 0]
# [2 1]]
x = np.array([[[0, 1], [1, 0]], [[0, 1], [1, 0]], [[0, 0], [1, 0]]])
print(x)
# [[[0 1]
# [1 0]]
#
# [[0 1]
# [1 0]]
#
# [[0 0]
# [1 0]]]
print(np.shape(x)) # (3, 2, 2)
print(x.ndim) # 3
y = np.nonzero(x)
print(np.array(y))
# [[0 0 1 1 2]
# [0 1 0 1 1]
# [1 0 1 0 0]]
print(np.array(y).shape) # (3, 5)
print(np.array(y).ndim) # 2
print(y)
# (array([0, 0, 1, 1, 2], dtype=int64), array([0, 1, 0, 1, 1], dtype=int64), array([1, 0, 1, 0, 0], dtype=int64))
print(x[np.nonzero(x)])
#[1 1 1 1 1]


x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x)
# [[1 2 3]
# [4 5 6]
# [7 8 9]]
y = x > 3
print(y)
# [[False False False]
# [ True True True]
# [ True True True]]
y = np.nonzero(x > 3)
print(y)
# (array([1, 1, 1, 2, 2, 2], dtype=int64), array([0, 1, 2, 0, 1, 2], dtype=int64))
y = x[np.nonzero(x > 3)]
print(y)
# [4 5 6 7 8 9]
y = x[x > 3]
print(y)
# [4 5 6 7 8 9]



"""

 numpy.where(condition, [x=None, y=None])
  满足条件 condition ，输出 x ，不满足输出 y 。
  
  只有 condition ，没有 x 和 y ，则输出满足条件 (即非0) 元素的坐标 (等价于 numpy.nonzero )。这里的坐标以tuple的形式给出，通
常原数组有多少维，输出的tuple中就包含几个数组，分别对应符合条件元素的各维坐标。
  """
x = np.arange(10)
print(x)
# [0 1 2 3 4 5 6 7 8 9]
y = np.where(x < 5, x, 10 * x)
print(y)
# [ 0 1 2 3 4 50 60 70 80 90]
x = np.array([[0, 1, 2],
[0, 2, 4],
[0, 3, 6]])
y = np.where(x < 4, x, -1)
print(y)
# [[ 0 1 2]
# [ 0 2 -1]
# [ 0 3 -1]]

#没有x和y
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.where(x > 5)
print(y)
# (array([5, 6, 7], dtype=int64),)
print(x[y])
# [6 7 8]
y = np.nonzero(x > 5)
print(y)
# (array([5, 6, 7], dtype=int64),)
print(x[y])
# [6 7 8]
x = np.array([[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])
y = np.where(x > 25)
print(y)
# (array([3, 3, 3, 3, 3, 4, 4, 4, 4, 4], dtype=int64), array([0, 1, 2, 3, 4, 0, 1, 2, 3, 4], dtype=int64))
print(x[y])
# [26 27 28 29 30 31 32 33 34 35]
y = np.nonzero(x > 25)
print(y)
# (array([3, 3, 3, 3, 3, 4, 4, 4, 4, 4], dtype=int64), array([0, 1, 2, 3, 4, 0, 1, 2, 3, 4], dtype=int64))
print(x[y])
# [26 27 28 29 30 31 32 33 34 35]

"""
1. numpy.searchsorted(a, v[, side='left', sorter=None]) Find indices where elements should be inserted to maintain order.
a. a：一维输入数组。当 sorter 参数为 None 的时候， a 必须为升序数组；否则， sorter 不能为空，存放 a 中元素的 index ，用于
反映 a 数组的升序排列方式。
b. v：插入 a 数组的值，可以为单个元素， list 或者 ndarray 。
c. side：查询方向，当为 left 时，将返回第一个符合条件的元素下标；当为 right 时，将返回最后一个符合条件的元素下标。
d. sorter：一维数组存放 a 数组元素的 index，index 对应元素为升序。

"""
x = np.array([0, 1, 5, 9, 11, 18, 26, 33])
y = np.searchsorted(x, 15)
print(y) # 5
y = np.searchsorted(x, 15, side='right')
print(y) # 5
y = np.searchsorted(x, -1)
print(y) # 0
y = np.searchsorted(x, -1, side='right')
print(y) # 0
y = np.searchsorted(x, 35)
print(y) # 8
y = np.searchsorted(x, 35, side='right')
print(y) # 8
y = np.searchsorted(x, 11)
print(y) # 4
y = np.searchsorted(x, 11, side='right')
print(y) # 5
y = np.searchsorted(x, 0)
print(y) # 0
y = np.searchsorted(x, 0, side='right')
print(y) # 1
y = np.searchsorted(x, 33)
print(y) # 7
y = np.searchsorted(x, 33, side='right')
print(y) # 8
x = np.array([0, 1, 5, 9, 11, 18, 26, 33])
np.random.shuffle(x)
print(x) # [33 1 9 18 11 26 0 5]
x_sort = np.argsort(x)
print(x_sort) # [6 1 7 2 4 3 5 0]
y = np.searchsorted(x, [-1, 0, 11, 15, 33, 35], sorter=x_sort)
print(y) # [0 0 4 5 7 8]
y = np.searchsorted(x, [-1, 0, 11, 15, 33, 35], side='right', sorter=x_sort)
print(y) # [0 1 5 5 8 8]


"""
计数
"""
x = np.count_nonzero(np.eye(4))
print(x) # 4
x = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]])
print(x) # 5
x = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]], axis=0)
print(x) # [1 1 1 1 1]
x = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]], axis=1)
print(x) # [2 3]
