import numpy as np
from D_数据分析.numpy包 import test
#数组的组合

x = np.array([1, 2, 3])
print(x)
y = np.array([7, 8, 9])
print(y)
z = np.concatenate([x, y])# 列表join操作
print(z)
"测试能不能连接两个数组"
test_recived=np.concatenate([test.create_ones(3),test.creat_eyes(3)])
print(test_recived,'\n')#说明concatenate这个方法是沿着方向

#testing
"""
重构数组
"""
# recived = test.use_array().shape
# print(recived)#（r，c）
# print(test.use_array().transpose())
# print("print\n")
# print(np.transpose(test.use_array()))
# reconstruct =np.reshape(test.use_array(),-1)
# print("这会输出一个一维列表")
# print(reconstruct)


#沿着新的轴加入一系列数组
x = np.array([1, 2, 3])
y = np.array([7, 8, 9])
z = np.stack([x, y])
print(z)
print(z.shape)  # (2, 3) print(z)
test_recived=np.stack([test.create_ones(3),test.creat_eyes(3)])
print(test_recived)

"""
总结一下：

--------------------------------------------------------------------------------------------------------------------------
concatenate([x, y])是直接把 后值接在后面，
如 [1 2 3]和[4 5 6]变成 [ 1 2 3 4 5 6]

stack([x, y]) 拼接：是把后面一个的元素整个包含原来的结构一起拼接
如：如 [1 2 3]和[4 5 6]变成 [ [1 2 3],[4 5 6]]


--------------------------------------------------------------------------------------------------------------------------

concatenate在行上相加axis=0   axis=1在列上相加

"""
x = np.array([[1, 2, 3], [4, 5, 6]]) 
y = np.array([[7, 8, 9], [10, 11, 12]])
z=np.stack([x,y])
# [[[ 1  2  3]  这就是一个列表包含两个矩阵 这个列表中有2个矩阵
#   [ 4  5  6]]  矩阵的维度为 2行 3列
#                       所以z的形状为 2，2，3
#  [[ 7  8  9]
#   [10 11 12]]]
print(z,'\nz的形状')#
print('打印一下z的形状',z.shape)#(2, 2, 3)
new_z = np.stack([x,y],axis=1)
print('打印一下z的形状',new_z.shape)#(2, 3, 2)
print(new_z)
print("axis=2的时候",np.stack([x,y],axis=2))
"""
axis =0 代表最外层的[]  以此类推
为啥此时可以0-2（axis） 因为这里是三维の
"""

#数组的拆分
"""使用split（x_rectangle,[row,column]）"""
#我们设定的矩阵是3X4的形状
recived_value_y=np.split(test.create_arrays_new(),[1,3])
print(recived_value_y)
y = np.split(test.create_arrays_new(), [1, 3], axis=1)
print(y)

# numpy.vsplit(ary, indices_or_sections)  垂直切分是把数组按照高度切分
print('\n打印数组的行和列',test.create_arrays_new().shape)
y=np.vsplit(test.create_arrays_new(),3)#这是按照列来切分
print(y)

y=np.vsplit(test.create_arrays_new(),[1])
print(y)



#数组平铺
"""
numpy.tile(A, reps) Construct an array by repeating A the number of times given by reps.
tile 是瓷砖的意思，顾名思义，这个函数就是把数组像瓷砖一样铺展开来。
"""
x = np.array([[1, 2], [3, 4]])
print(x)
#现在进行平铺
y=np.tile(x,(1,3))#这里列表和元组是一样的
print(y)

y=np.tile(x,[1,3])
print(y)

y=np.tile(x,[3,1])
print(y)

y = np.tile(x, (3, 3))
print(y)

#添加和删除元素
"""
numpy.unique(ar, return_index=False, return_inverse=False,return_counts=False, axis=None) 
Find the unique elements of an array. a. return_index：the indices of the input array that give the unique values b. return_inverse：the indices of the unique array that reconstruct the input array c. return_counts：the number of times each unique value comes up in the input array
 
"""
'查找数组的唯一元素'
a=np.array([1,1,2,3,3,4,4])
b=np.unique(a,return_counts=True)
print(b)
print(b[0][list(b[1]).index(1)])
# https://blog.csdn.net/csdn15698845876/article/details/73380803
















