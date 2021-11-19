#导入包
import numpy as np
import json


#内容部分
"""
文本格式选项
np.set_printoptions(precision=4)限制小数点后几位,且只限制下一个语句

np.random.seed(1)控制随机数的个数
"""
print("判断set_printoptions的作用")
np.set_printoptions(precision=4)#控制文本的输出长度
x_1=np.array([1.1233456778])
print(x_1,end='\n')# [1.1233]


print("测试是否只是对相邻的语句起作用")
y_1=np.array((122324.343545456))#122324.343545456
print(y_1)


print("测试列表是否使用")
list_1=[]
for i in range(10):
    list_1.append(np.random.rand()*10)
print(list_1)
np.set_printoptions(precision=5)
z_1=np.array(list_1)
print("print z_1\n",z_1)

"""
np.set_printoptions(threshold=20)与上面的区别在于 这里写了一个threshold 阙值
目的就是限制输入的个数
而precision是限制输入的单个元素的值的小数点个数
"""
np.set_printoptions(threshold=20)
x = np.arange(50)
print(x) # [ 0 1 2 ... 47 48 49]
np.set_printoptions(threshold=np.iinfo(np.int).max)
print(x)
# [ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# 48 49]
"""
import numpy as np
a=np.array([[1],[2],[-1],[0]])
b=np.maximum(a,np.finfo(np.float32).eps)
print(b)
[[1.0000000e+00]
 [2.0000000e+00]
 [1.1920929e-07]
 [1.1920929e-07]]
"""
eps = np.finfo(float).eps#eps是取非负的最小值。
x = np.arange(4.)
x=x**2 - (x+eps)**2
print(x)
# [‐4.9304e‐32 ‐4.4409e‐16 0.0000e+00 0.0000e+00]
np.set_printoptions(suppress=True)
print(x) # [‐0. ‐0. 0. 0.]
x = np.linspace(0, 10, 10)
print(x)
# [ 0. 1.1111 2.2222 3.3333 4.4444 5.5556 6.6667 7.7778 8.8889
# 10. ]
np.set_printoptions(precision=2, suppress=True, threshold=5)
print(x) # [ 0. 1.11 2.22 ... 7.78 8.89 10. ]

#判断是否为空 并且打印
accepts=np.isnan(list_1)
print("\n",accepts)


x = np.get_printoptions()
print(x)
#{'edgeitems': 3, 'threshold': 5, 'floatmode': 'maxprec', 'precision': 2, 'suppress': True, 'linewidth': 75, 'nanstr': 'nan', 'infstr': 'inf', 'sign': '-', 'formatter': None, 'legacy': False}




