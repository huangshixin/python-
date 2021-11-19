import torch
import numpy as np
'''
本章节主要目的是对比numpy中已有的方法     tensor张量
'''
x=torch.empty(5,3)


x=torch.rand(5,3)

x = torch.zeros(5, 3, dtype=torch.long)


x = torch.tensor([5.5, 3])#根据数据创建  tensor 相当于一个ndarry

print(x.size())
print(x.shape)


'''
函数 	功能
Tensor(*sizes) 	基础构造函数
tensor(data,) 	类似np.array的构造函数
ones(*sizes) 	全1Tensor
zeros(*sizes) 	全0Tensor
eye(*sizes) 	对角线为1，其他为0
arange(s,e,step) 	从s到e，步长为step
linspace(s,e,steps) 	从s到e，均匀切分成steps份
rand/randn(*sizes) 	均匀/标准分布
normal(mean,std)/uniform(from,to) 	正态分布/均匀分布
randperm(m) 	随机排列
'''

'''算术运算'''
# y = torch.rand(5, 3)
# print(x + y)
#
# print(torch.add(x, y))
#
# result = torch.empty(5, 3)
# torch.add(x, y, out=result)
# print(result)
#
# y.add_(x)
# print(y)


'''
改变形状

tensor和数据是同一种概念


x = torch.arange(1, 3).view(1, 2)

y = torch.arange(1, 4).view(3, 1)


x = torch.arange(1, 3).reshape((1, 2))

y = torch.arange(1, 4).reshape((3, 1))


注意view()返回的新Tensor与源Tensor虽然可能有不同的size，但是是共享data的，也即更改其中的一个，另外一个也会跟着改变。
'''



#pytorch提供了一个方法clone 克隆

# x_cp = x.clone().view(15)
# x -= 1
# print(x)
# print(x_cp)




#tensor on GPU

'''
用 to()可以将Tensor在cpu和gpu之间相互移动

'''

if torch.cuda.is_available():
    device =torch.device('cuda') #GPU
    y =torch.ones_like(x,device=device)
    x=x.to(device)
    z=x+y
    print(z)
    print(z.to("cpu",torch.double))






'''
线性代数
'''
# 函数 	功能
# trace 	      对角线元素之和(矩阵的迹)
# diag 	          对角线元素
# triu/tril 	  矩阵的上三角/下三角，可指定偏移量
# mm/bmm 	      矩阵乘法，batch的矩阵乘法
# addmm/addbmm/addmv/addr/baddbmm.. 	矩阵运算
# t 	          转置
# dot/cross 	   内积/外积
# inverse 	      求逆矩阵
# svd 	          奇异值分解





'''
广播机制
'''
x = torch.arange(1, 3).view(1, 2)
print(x)
y = torch.arange(1, 4).view(3, 1)
print(y)
print(x + y)


#
# tensor([[1, 2]])

# tensor([[1],
#         [2],
#         [3]])

# tensor([[2, 3],
#         [3, 4],
#         [4, 5]])


'''
tensor转numpy

我们很容易用numpy()和from_numpy()将Tensor和NumPy中的数组相互转换。
但是需要注意的一点是： 
这两个函数所产生的的Tensor和NumPy中的数组*&****************共享相同的内存**********************（所以他们之间的转换很快），改变其中一个时另一个也会改变！！！
'''
a = torch.ones(5)
b =a.numpy()
print(a, b)

a += 1
print(a, b)
b += 1
print(a, b)

a = np.ones(5)
b = torch.from_numpy(a)
print(a, b)

a += 1
print(a, b)
b += 1
print(a, b)





"""
----------------------
运算的内存开销

索引操作不会开辟新的内存，但是运算会开辟新的内存 然后将y指向新的内存

用python自带的id函数 如果两个实例一样返回true 反之 false
----------------------
"""
x=torch.tensor([1,2])
y=torch.tensor([3,4])
id_before =id(y)
y=y+x
print(id(y) ==id_before)













