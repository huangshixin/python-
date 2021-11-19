import numpy as np
import matplotlib.pyplot as plt

#数组操作
"""
reshape 是重构’数组‘
column=np.reshape(x,[：,-1])
shape 是输出’数组‘的长度
transpose 数组的转置
x = np.random.rand(5, 5) * 10
print('\n',np.random.rand(3))
print('打印数据结构\n',x)
x = np.around(x, 2)#保留小数点后一位
"""

"更改形状"
"""
numpy.ndarray.shape 表示数组的维度，返回一个元组
所以可以通过数组下角标去取
"""
x = np.array([1, 2, 9, 4, 5, 6, 7, 8])
print(x.shape)#（8，） 因为没有列
print(x.shape[0])#在一维数组的时候设置为0
x.shape=[2,4]
print(x)


#迭代器
x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
print(x.shape)#（5，5）
print(x.shape[0],x.shape[1])
"将数组转换为一维的迭代器，可以用for访问数组每一个元素"
y=x.flat
print(y)
for i in y:
    print(i,end=' ') # end=' ' 为了输出时候有空格
print('\n')


#ravel()返回的是       ###视图###
" numpy.ravel(a, order='C')"
#ravel 可以理解为把x矩阵转化为列表存储 并输出
y = np.ravel(x)#
print(y)#这里y是一个列表
y[3]=0
print('打印由ravel方法创造的视图的某个位置的值','\n')
print(y[x.shape[0]*x.shape[1]-3])#这就验证了ravel将列表传给了y
print('虽然你修改了y[3],但是y是由x.ravel赋值的,numpy当中的视图和数据库中的概念不一致，视图的改变会影响原来的值 ')
print(x)
print(y)


#reshape: 在不改变数据的情况下 把数组的形状进行改变
" reshape() 函数当参数 newshape = [rows,-1] 时，将根据行数自动确定列数"
"numpy.reshape(a, newshape[, order='C']) "
x=np.arange(12)
y =np.reshape(x,[3,4],order='F') #c是按横着排  F是列着排
print(y)



#python提供了           自动确定               列数的功能
"塑造一个4x3的矩阵然后使用reshape将它转置"
x = np.arange(12)#0-11
x.shape=[4,3]#python提供了一种将arange列表转化为矩阵的方式
print(x)
print("打印3x4的矩阵")
y = np.reshape(x, [3, 4])
print(y.dtype)  # int32
print("打印4x3的矩阵")
column=np.reshape(x,[3,-1]) #让python自己去计算列的值
print(column)
row = np.reshape(x,[-1,6])#你是重塑 你必须先告诉系统需要的行或者列
print(row)

"需要特别注意的是" \
" reshape() 函数当参数 newshape = -1 时，表示将数组降为一维。"
y=np.reshape(x,-1) #column=np.reshape(x,[3,-1])
print('打印结果y的数据结构',y)
for i in y:
    print(i,end='\t')


"数组的转置"
#在random的rand方法中  我们会自动生成一个0-1内的值，
# 它根据我们传入的数值给我们返回一个数据结构
#可能是列表 也可能是数组
#取决于 rand() 里面传入的值
x = np.random.rand(5, 5) * 10
print('\n',np.random.rand(3))
print('打印数据结构\n',x)
x = np.around(x, 2)#保留小数点后一位
print(x)
"实现转置功能  使用transpose（）"
print(x.transpose())#python自带的
print("又或者使用")
print(np.transpose(x))#这是numpy提供的


"更改维度"
# 当创建一个数组之后，还可以给它增加一个维度，这在矩阵计算中经常会用到。
# 1. numpy.newaxis = None None 的别名，对索引数组很有用
x = np.array([1, 2, 9, 4, 5, 6, 7, 8])
print(x.shape)  # (8,)
print(x)  # [1 2 9 4 5 6 7 8]
###################################
y=x[np.newaxis,:]
print(y.shape)
print(y,'\n')
###################################
y=x[:,np.newaxis]
print(y.shape)
print(y)

"numpy.squeeze(a, axis=None) 从数组的形状中删除单维度条目，即把shape中为1的维度去掉。 "
#a表示输入的数组
#b    axis用于指定需要删除的维度  必须是单维度
"""在机器学习和深度学习中，通常算法的结果是可以表示向量的数组（即包含两对或以上的方括号形式[[]]），
如果直接利用这个数组进行画图 可能显示界面为空（见后面的示例）。我们可以利用 squeeze() 函数将表示
向量的数组转换为秩为1的数组，这样利用 matplotlib 库函数画图时，就可以正常的显示结果了。
"""
x = np.arange(10)
print(x.shape)  # (10,)
x = x[np.newaxis, :]#给数组增加一个维度
print(x.shape)  # (1, 10)
y = np.squeeze(x)#我们可以利用 squeeze() 函数将************ 表示向量  **********的数组转换为秩为1的数组，
print('**********************')
print(y.shape)  # (10,)
print('**********************')

x=np.array([1,3,45,56,6,76,78,3,8,8,6,12])
accept_x=x[np.newaxis,:] #accept_x=x[np.newaxis,:] 在指定的位置加上一个维度
print(accept_x)
x = np.array([[[0], [1], [2]]])
print(x.shape)  # (1, 3, 1)
print(x)
" axis用于指定需要删除的维度  必须是单维度"
y=np.squeeze(x)
print(y.shape)
print(y)

y = np.squeeze(x, axis=0)
print(y.shape)  # (3, 1)
print(y) # [[0] #  [1] #  [2]]
y = np.squeeze(x, axis=2)
print(y.shape)  # (1, 3)
print(y)  # [[0 1 2]


x=np.array([[1,4,9,16,25]])
x= np.squeeze(x)
print(x.shape)#列表中存了个列表  一行五列
plt.plot(x)
plt.show()
create_random_array(3,4)
print(create_random_array())











