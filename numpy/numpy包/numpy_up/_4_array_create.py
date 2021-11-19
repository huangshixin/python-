import numpy as np
"""
type()是看你是什存储类型 比如list  、array  、ndarray
A.dtype 查看A的数据类型

###############################################################
1. arange(start,stop ,stride) 函数：返回给定间隔内的均匀间隔的值。 
2. linspace() 函数：返回指定间隔内的等间隔数字。 返回等差数列
3. logspace() 函数：返回数以对数刻度均匀分布。 
4. numpy.random.rand() 返回一个由[0,1)内的随机数组成的数组
5、array创建出来的是一种数据结构 叫ndarray
6. empty_like 函数：返回与给定数组具有相同形状和类型的新数组

1. eye() 函数：返回一个对角线上为1，其它地方为零的单位数组。 
2. identity() 函数：返回一个方的单位数组
3. diag()函数：提取对角线或构造对角数组
###################################################################
"""
#通过array创建数组  def array(p_object, dtype=None, copy=True, order='K', subok=False, ndmin=0):
"""创建一维数组
array创建出来的是一种数据结构 叫ndarray
"""
array_a =np.array([0,1,2,3,4])
array_b =np.array((0,1,2,3,4))
print(array_a,type(array_a))
print(array_b,type(array_b))
"""创建二维数组"""
#二维数组就是在array的情况之下 去用一个列表存放多个列表的情况。
array_c= np.array([[11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20],
                   [21, 22, 23, 24, 25],
                   [26, 27, 28, 29, 30],
                   [31, 32, 33, 34, 35]])
print(array_c,type(array_c))
"""创建三维数组"""
d = np.array([[(1.5, 2, 3), (4, 5, 6)],
              [(3, 2, 1), (4, 5, 6)]])
print(d, type(d))



#4.1.2 通过asarray()函数进行创建
"""
array() 和 asarray() 主要区别就是当数据源是ndarray 时， array() 仍 然会 copy 出一个副本，占用新的内存，但不改变 dtype 时 asarray() 不会。
"""
#array() 和 asarray() 都可以将结构数据转化为 ndarray
x = [[1, 1, 1], [1, 1, 1], [1, 1, 1]] #对于x而言它是一个列表存列表的形式
y = np.array(x)#array将x转为ndarray的形式 np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
z= np.asarray(x)
x[1][2]=2
print(x,type(x))
print('\n')
print(y,type(y),y.dtype)
print('\n')
print(z,type(z),z.dtype)
#更改为较大的dtype时，其大小必须是array的后一个axis的总大小（以字节为单位）的除数
"""
x = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) 
print(x, x.dtype) # [[1 1 1] #  [1 1 1] #  [1 1 1]] int32 x.dtype = np.float
# ValueError: When changing to a larger dtype, its size must be a divisor of the total size in bytes of the last axis of the array.

"""

#通过fromfunction()函数进行创建
def fromfunction(function,shape,**kwargs):
    pass

def f(x,y):
    return  10*x*y

x= np.fromfunction(f,(5,4),dtype=int)
print(x)

y=np.fromfunction(lambda i ,j:i==j,(3,3),dtype=int)
print(y)



#ones 和zeros的填充方式
"""
dtype：是你的属性类型
order：是排序方式
def zeros(shape, dtype=None, order='C'):
def zeros_like(a, dtype=None, order='K', subok=True, shape=None):返回与给定数组形状和类型相同的零数组
"""
list_zeros = np.zeros((4,5))#np.zeros([4,5])也可以
list_zeros_2 = np.zeros(10)
list_copy_zeros = np.zeros_like(list_zeros)#返回给定数组或者列表一样的数组
print(list_zeros,'\n')
print(list_zeros_2,'\n')
print(list_copy_zeros)
#同理ones数组当中也有类似的方法  ones_like()
list_ones = np.ones(4)#生成列表
array_ones= np.ones((3,5))#生成数组
print(list_ones)
print(array_ones)



#空数组
"""
1. empty() 函数：返回一个空数组，数组元素为随机数。
2. empty_like 函数：返回与给定数组具有相同形状和类型的新数组
"""
null_empty = np.empty(5)#返回一个空的数组 数值是固定的
print(null_empty)
#同理返回一个空的矩阵
null_actangle = np.empty((3,3))
print(null_actangle)

null_new_actangle = np.empty_like([[1,2,3],[4,5,6]])#返回的是一个int型
print(null_new_actangle)


#4.2.4 单位数组

"""
ctr+d 复制到下一行
1. eye() 函数：返回一个对角线上为1，其它地方为零的单位数组。 
2. identity() 函数：返回一个方的单位数组
3. diag()函数：提取对角线或构造对角数组
"""
single_array = np.eye(5)#返回是一个数组不是矩阵
print(single_array)
# single_arrays = np.eye((3,5))错误示范
# print(single_arrays)



#4.3.6 常数数组
"""
1. full() 函数：返回一个常数数组。 
2. full_like() 函数：返回与给定数组具有相同形状和类型的常数数组。
"""



#利用数组范围来创建ndarray

"""
1. arange(start,stop ,step) 函数：返回给定间隔内的均匀间隔的值。 
2. linspace() 函数：返回指定间隔内的等间隔数字。 
3. logspace() 函数：返回数以对数刻度均匀分布。 
4. numpy.random.rand() 返回一个由[0,1)内的随机数组成的数组
"""
# def arange([start,] stop[, step,], dtype=None):
#     pass
# def linspace(start, stop, num=50, endpoint=True, retstep=False,              dtype=None, axis=0):
# def logspace(start, stop, num=50, endpoint=True, base=10.0,              dtype=None, axis=0):
# def rand(d0, d1, ..., dn):
arange_x = np.arange(5) #返回一个0-5的列表
print(arange_x)
arange_y= np.arange(3,7,2)#从3-6 步长为2
print(arange_y)













#######################################################################
arange_z= np.linspace(start=0,stop=2,num=5)#均匀分布
########################################################################














print(arange_z)
arange_x=np.logspace(0,1,5)
arange_y=np.random.random(6)
print(arange_x)










