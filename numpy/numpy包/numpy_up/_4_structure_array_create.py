#结构数组
import  numpy as np
import random
"""
1. numpy.ndarray.ndim 用于返回数组的维数（轴的个数）也称为秩，一维数组的秩为 1，二维数组的秩为 2，以此类推。 
2. numpy.ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性(秩)。 
3. numpy.ndarray.size 数组中所有元素的总量，相当于数组的 shape 中所有元素的乘积，例如矩阵的元素总量为行与列的乘积。
4. numpy.ndarray.dtype ndarray 对象的元素类型。 
5. numpy.ndarray.itemsize 以字节的形式返回数组中每一个元素的大小。
"""

#副本与视图
#Numpy中，尤其是在做数组运算或数组操作时，返回的不是数组的副本就是视图
""" int > float > str  的 向下转型"""
a = np.array([1, 2, 3, 4, 5])
print(a)  # [1 2 3 4 5]
b = np.array([1, 2, 3, 4, '5'])
print(b)  # ['1' '2' '3' '4' '5']
c = np.array([1, 2, 3, 4, 5.0])
print(c)  # [1. 2. 3. 4. 5.]

y=np.array([1,2,3,4,5,6,7,8])
z=y.copy()
y[0]=-1
print(y)


###################################################################
def array(length,lengths):
    arrays = np.ones((length,lengths))
    arrays[::2, ::3] =-1#行（0，2，4） 列（0，3）
    return arrays
print(array(5,6))









#索引和切片
# print(31页)


