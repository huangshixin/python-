import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

'''矩阵和向量积'''
print('第一：计算矩阵或者向量的内积 用np.dot')

'''numpy.dot(a, b[, out]) 计算两个矩阵的乘积，如果是一维数组则是它们的内积。'''
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])
print('计算一维数组的内积：\n ',np.dot(x,y),end='\n')

x=np.arange(1,13).reshape((4,3))
y=np.array([[5, 4, 2], [1, 7, 9], [0, 4, 5]])
print('\n计算矩阵的内积：（4x3） *（3x3）型的矩阵\n',np.dot(x,y),end='\n')







'''矩阵特征值与特征向量'''

'''method
numpy.linalg.eig(a) 计算方阵的特征值和特征向量。
numpy.linalg.eigvals(a) 计算方阵的特征值。
'''
print('\n矩阵特征值与特征向量\n')
#创建一个对角矩阵
x=np.diag((1,2,3))#对角线元素的值为 1 2 3
print('diag 传入一个列表或者元组 打印出以该列表（元组）的值为对角线的矩阵\n',x)

a,b=np.linalg.eig(x)
print('\nnumpy.linalg.eig(a) 既返回特征值 也返回特征向量\n',a,'\n',b,end='\n')
print('\nnumpy.linalg.eigvals(a) 计算方阵的特征值:\n',np.linalg.eigvals(x))

print('\n检验特征值与特征向量是否正确\n')
for i in range(3):
    #线性代数中有个公式 ：特征值*特征向量==矩阵*特征向量
    if np.allclose(a[i]*b[:,i], np.dot(x, b[:, i])):
        print('right')
    else:
        print('Error')
print('\n一般而言我们认知的矩阵*特征向量应该是==一个向量， 但是对于numpy中  matrix multiply feature vector ==new matrix \n')








print('\n判断对称矩阵是否为正定矩阵（特征值是否全部为正）\n')
A=np.arange(16).reshape((4,-1))
print(A)
print('\n打印A的转置\n',A.T)
A=A+A.T
print('\n打印A+A.T：\n',A)
print('\n打印B的特征向量：',np.linalg.eigvals(A),end='\n')







'''矩阵的奇异分解
u, s, v = numpy.linalg.svd(a, full_matrices=True, compute_uv=True, hermitian=False) 奇异
值分解
a 是一个形如(M,N)矩阵
full_matrices 的取值是为False或者True，默认值为True，这时 u 的大小为(M,M)， v 的
大小为(N,N)。否则 u 的大小为(M,K)， v 的大小为(K,N) ，K=min(M,N)。
compute_uv 的取值是为False或者True，默认值为True，表示计算 u,s,v 。为False的时候
只计算 s 。


总共有三个返回值 u,s,v ， u 大小为(M,M)， s 大小为(M,N)， v 大小为(N,N)， a =
u*s*v 。


其中 s 是对矩阵 a 的奇异值分解。 s 除了对角元素不为 0 ，其他元素都为 0 ，并且对角元
素从大到小排列。 s 中有 n 个奇异值，一般排在后面的比较接近0，所以仅保留比较大的 r
个奇异值。
'''
print('\n矩阵的奇异分解\n')
A = np.array([[4, 11, 14], [8, 7, -2]])
print(A)
# [[ 4 11 14]
# [ 8 7 ‐2]]
print('\n学习使用 numpy.linalg.svd函数\n ')
u, s, vh = np.linalg.svd(A, full_matrices=False)
print('\n该函数每次返回三个元素 U S V \n')
print('\nU代表一种矩阵的形状 比如matrix A是[4x5],则返回（4，4）.'
      '实际上矩阵A是mxn型就打印'
      '（M,M)\n',u.shape) # (2, 2)
print('\n打印u\n',u)
print('\ns是对称矩阵a的奇异分解，A是M,N型 则返回（M,N)\n',s.shape) # (2,)
print(np.diag(s))
# [[18.97366596 0. ]
# [ 0. 9.48683298]]
print('\n它是N,N形状：\n',vh.shape) # (2, 3)
print(vh)
# [[‐0.33333333 ‐0.66666667 ‐0.66666667]
# [ 0.66666667 0.33333333 ‐0.66666667]]
a = np.dot(u, np.diag(s))
a = np.dot(a, vh)
print(a)
print('svd方法目的是打印出 S（mxm）   V（m,)   d(n,n)  而矩阵A=s*v*d')


'''奇异分解的举例子'''
print('\n奇异分解的举例子\n')
A = np.array([[1, 1], [1, -2], [2, 1]])
print(A)
# [[ 1 1]
# [ 1 ‐2]
# [ 2 1]]
u, s, vh = np.linalg.svd(A, full_matrices=False)
print(u.shape) # (3, 2)
print(u)
# [[‐5.34522484e‐01 ‐1.11022302e‐16]
# [ 2.67261242e‐01 ‐9.48683298e‐01]
# [‐8.01783726e‐01 ‐3.16227766e‐01]]
print(s.shape) # (2,)
print(np.diag(s))
# [[2.64575131 0. ]
# [0. 2.23606798]]
print(vh.shape) # (2, 2)
print(vh)
# [[‐0.70710678 ‐0.70710678]
# [‐0.70710678 0.70710678]]
a = np.dot(u, np.diag(s))
a = np.dot(a, vh)
print(a)
# [[ 1. 1.]
# [ 1. ‐2.]
# [ 2. 1.]]

print('\n')





'''矩阵的QR分解'''






