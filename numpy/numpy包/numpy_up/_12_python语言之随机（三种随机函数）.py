import numpy as np
from numpy import random as nr
import random as rd
"""
numpy.random模块中提供啦大量的随机数相关的函数。

1 numpy中产生随机数的方法

　　1)rand() 　　产生[0,1]的浮点随机数,括号里面的参数可以指定产生数组的形状

　　2)randn()　　产生标准正太分布随机数，参数含义与random相同

　　3)randint()　　产生指定范围的随机数，最后一个参数是元祖，他确定数组的形状

"""
#只显示小数点后两位

print(np.set_printoptions(2))
r1 = nr.rand(3,4)#产生一个矩阵 0-1之间的数
print(r1,end='\n')
r2 = nr.randn(5,4)#产生一个正太分布
print(r2,end='\n')
r3 = nr.randint(0,10,size = (4,3))#在0-10当中随机产生一个随机数
print(r3,end='\n')



#常用的分布

"""
　　1）normal()　　正太分布

　　2）uniform()　　均匀分布

　　3）poisson()　　泊松分布
"""


"""
permutation()随机生成一个乱序数组，当参数是n时，返回[0,n)的乱序，他返回一个新数组。
shuffle()则直接将原数组打乱。
choice（）是从指定的样本中随机抽取
"""
new_x=np.random.permutation(10)
print(new_x)
new_y=nr.shuffle(new_x)#[9 0 7 6 2 3 8 5 4 1]
print(new_y,end='\n')
print(nr.choice(new_x,3))






















