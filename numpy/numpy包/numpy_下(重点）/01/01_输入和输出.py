import json
import  numpy as np

"""
输入和输出
numpy二进制文件

save（）、savez（）、load（）函数以numpy专用的二进制类型（npy。npz）保存和读取数据
save()就是把文件保存到npy或者npz文件当中去


savez（）保存后的文件肯定是压缩包的形式
**，其中每个文件都是一个 save() 保存的npy文件，
文件名对应于数组名。 load() 自动识别npz文件，并且返回一个类似于字典的对象，可以通过数组名
作为关键字获取数组的内容。


load（）就是加载文件的信息到内存当中去
npy是什么格式呢？
以二进制的方式存储文件，在二进制文件第一行以文本的现实保存了数据的元信息（ndim
dtype、shape）

npz是什么格式呢？
以压缩打包的方式存储文件，可以用压缩软件解压
"""
############################################################################################################################
"""
专题：
uniform 可以实现，（A,B,[C,D])在AB区间内生成，cxd规模的随机数

rand(A) 生成A个 0-1的随机数 

rand(A,B) 返回一个矩阵AXB  其中各行各列都是0-1的数

numpy.save(file,arr,allow_pickle=True,fix_imports=True)

numpy.load(file,mmap_mode=None,allow_pickle=Flase,fix_imports=True,encoding='ASCII')
"""

outfile=r'.\test.npy'#定义文件名
x=np.random.uniform(3,5,(3,5))#生成一个0-1的随机数，且这个规模是
np.save(outfile,x)#numpy中把数据写道outfile里面去 save要识别npy文件，而且save判断的是当下的目录
y=np.load(outfile)#把文件数据加载到内存
print(y,end='\n')


#######################################################################################################



"""
#将多个数组保存到一个文件中去
numpy.savez()

*******npz  json  npy文件都是用load加载到内存*******
"""

outfile_2=r'.\test.npz'
x=np.linspace(0,np.pi,5)
y=np.sin(x)
z=np.cos(x)
np.savez(outfile_2,x,y,z)#savez 你可以理解为，把xyz三个列表的值存到outfile_2的文件中的三个文件夹去
"""
x y z 是三个列表  其中都包含一定的值 他们分别存放在三个文件夹下，
他们汇总到一个outfile_2压缩文件下
z_d=z  相当于给z文件夹重新命名
如果没有重新命名的话 就是arr_  的递增
"""
print('''x y z 是三个列表  其中都包含一定的值 他们分别存放在三个文件夹下，
他们汇总到一个outfile_2压缩文件下
z_d=z  相当于给z文件夹重新命名
如果没有重新命名的话 就是arr_  的递增''')
data=np.load(outfile_2)
np.set_printoptions(suppress=True)
print(data.files)
print(data['arr_0'])
print(data['arr_1'])
print(data['arr_2'],end='\n')
# ['z_d', 'arr_0', 'arr_1']
# [0.         0.78539816 1.57079633 2.35619449 3.14159265]
# [0.         0.70710678 1.         0.70710678 0.        ]
# [ 1.          0.70710678  0.         -0.70710678 -1.        ]
"""
用解压软件打开 test.npz 文件，会发现其中有三个文件： arr_0.npy,arr_1.npy,z_d.npy ，其中分别
保存着数组 x,y,z 的内容。
"""




##################################################################



"""
txt 和CSV文件是数据集中常用的文件名


******都是用loadtxt（）来加载到内存

savetxt() ， loadtxt() 和 genfromtxt() 函数用来存储和读取文本文件（如TXT，CSV等）。
numpy.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='',
comments='# ', encoding=None) Save an array to a text file.
fname：文件路径
X：存入文件的数组。
fmt：写入文件中每个元素的字符串格式，默认'%.18e'（保留18位小数的浮点数形式）。
delimiter：分割字符串，默认以空格分隔。


genfromtxt() 比 loadtxt() 更加强大，可对缺失数据进行处理。
numpy.loadtxt(fname, dtype=float, comments='#', delimiter=None, converters=None,
skiprows=0, usecols=None, unpack=False, ndmin=0, encoding='bytes', max_rows=None)

"""

#eg  开始写入和读出txt文件
print("开始写入和读出txt文件")
outfile=r'.\new_read.txt'
x=np.arange(0,10).reshape(2,-1)
# y=np.arange(1,5)
np.savetxt(outfile,x)#只能存一个
print(np.loadtxt(outfile),end='\n')
# [[0. 1. 2. 3. 4.]
# [5. 6. 7. 8. 9.]]


#开始读取和写入信息到CSV
print("#开始读取和写入信息到CSV")
outfile = r'.\new_test.csv'
x = np.arange(0, 10, 0.5).reshape(4,-1)
np.savetxt(outfile, x, fmt='%.3f', delimiter=',')#fmt 保留几位小数  delimiter 用  什么字符分割
y = np.loadtxt(outfile, delimiter=',')
print(y,end='\n')
# [[0. 0.5 1. 1.5 2. ]
# [2.5 3. 3.5 4. 4.5]
# [5. 5.5 6. 6.5 7. ]
# [7.5 8. 8.5 9. 9.5]]



#genfromtxt() 是面向结构数组和缺失数据处理的。
print("genfromtxt() 是面向结构数组和缺失数据处理的。")
outfile=r'.\data.csv'
x=np.loadtxt(outfile,delimiter=',',skiprows=1)
print(x)
y=np.loadtxt(outfile,delimiter=',',skiprows=2)
print(y)
# [[  1.  123.    1.4  23. ]
# #  [  2.  110.    0.5  18. ]
# #  [  3.  164.    2.1  19. ]]
# # [[  2.  110.    0.5  18. ]
# #  [  3.  164.    2.1  19. ]]
x = np.loadtxt(outfile, delimiter=',', skiprows=1, usecols=(1, 2))
print(x)
# [[123. 1.4]
# [110. 0.5]
# [164. 2.1]]
val1, val2 = np.loadtxt(outfile, delimiter=',', skiprows=1, usecols=(1, 2), unpack=True)
print(val1) # [123. 110. 164.]
print(val2) # [1.4 0.5 2.1]
outfile = r'.\data.csv'
x = np.genfromtxt(outfile, delimiter=',', names=True)
print(x)
# [(1., 123., 1.4, 23.) (2., 110., 0.5, 18.) (3., 164., 2.1, 19.)]
print(type(x))
# <class 'numpy.ndarray'>
print(x.dtype)
# [('id', '<f8'), ('value1', '<f8'), ('value2', '<f8'), ('value3', '<f8')]
print(x['id']) # [1. 2. 3.]
print(x['value1']) # [123. 110. 164.]
print(x['value2']) # [1.4 0.5 2.1]
print(x['value3']) # [23. 18. 19.]
#
#
#
# ########################################################################################
#
# """文本格式选项"""
# np.set_printoptions(precision=4)
# x = np.array([1.123456789])
















