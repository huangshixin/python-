import numpy as np

"""
解释说明一下什么是QR分解


一个矩阵A是mxn的形状， 且m>n 则它可以分解为A=QR，其中
Q属于mxm型的正交矩阵
R=[R‘,0] R是一个mxn型
R'是nxn型  且是上三角矩阵


Q.T *Q==Q*Q.T=I (I是单位矩阵）

"""




'''
q,r = numpy.linalg.qr(a, mode='reduced') 计算矩阵 a 的QR分解。
a 是一个(M, N)的待分解矩阵。
mode = reduced ：返回(M, N)的列向量两两正交的矩阵 q ，和(N, N)的三角阵
r （Reduced QR分解）。
mode = complete ：返回(M, M)的正交矩阵 q ，和(M, N)的三角阵 r （Full QR分解）。
'''
A = np.array([[2, -2, 3], [1, 1, 1], [1, 3, -1]])
print('\na 是一个(M, N)的待分解矩阵。\n',A)
# [[ 2 ‐2 3]
# [ 1 1 1]
# [ 1 3 ‐1]]
q, r = np.linalg.qr(A)
print('\n np.linalg.qr(A)生成两个形状 首先是：q\n',q.shape) # (3, 3)
print(q)
# [[‐0.81649658 0.53452248 0.21821789]
# [‐0.40824829 ‐0.26726124 ‐0.87287156]
# [‐0.40824829 ‐0.80178373 0.43643578]]
print('\n其次是r矩阵\n',r.shape) # (3, 3)
print(r)
# [[‐2.44948974 0. ‐2.44948974]
# [ 0. ‐3.74165739 2.13808994]
# [ 0. 0. ‐0.65465367]]
print('\n利用dot方法进行QR点乘计算A\n',np.dot(q, r))
# [[ 2. ‐2. 3.]
# [ 1. 1. 1.]
# [ 1. 3. ‐1.]]
a = np.allclose('\n判断q是不是正交矩阵\n',np.dot(q.T, q), np.eye(3))
print(a) # True