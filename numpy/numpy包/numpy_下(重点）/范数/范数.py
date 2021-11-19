#矩阵的范数
import numpy as np
'''
numpy.linalg.norm(x, ord=None, axis=None, keepdims=False) 
'''
from numpy import linalg as lg
from numpy import linspace as ls




'''求向量的范数'''
x = np.array([1, 2, 3, 4])
print('''在numpy.linalg.norm中的作用就是求范数\n
ord=None 则默认是 二范数\n
ord=1 相当于一范数\n
ord=np.inf  相当于无穷范数''')

print(np.linalg.norm(x, ord=1))
# 10.0
print(np.sum(np.abs(x)))
# 10
print(np.linalg.norm(x, ord=2))
# 5.477225575051661
print(np.sum(np.abs(x) ** 2) ** 0.5)#abs相当于求绝对值
# 5.477225575051661
print(np.linalg.norm(x, ord=-np.inf))#计算无穷范数
# 1.0
print(np.min(np.abs(x)))
# 1
print(np.linalg.norm(x, ord=np.inf))
# 4.0
print(np.max(np.abs(x)))


A = np.array([[1, 2, 3, 4], [2, 3, 5, 8],
[1, 3, 5, 7], [3, 4, 7, 11]])
print(A)
# [[ 1 2 3 4]
# [ 2 3 5 8]
# [ 1 3 5 7]
# [ 3 4 7 11]]
print(np.linalg.norm(A, ord=1)) # 30.0
print(np.max(np.sum(A, axis=0))) # 30
print(np.linalg.norm(A, ord=2))
# 20.24345358700576
print(np.max(np.linalg.svd(A, compute_uv=False)))
# 20.24345358700576
print(np.linalg.norm(A, ord=np.inf)) # 25.0
print(np.max(np.sum(A, axis=1))) # 25
print(np.linalg.norm(A, ord='fro'))
# 20.273134932713294
print(np.sqrt(np.trace(np.dot(A.T, A))))







'''计算方阵的行列式'''
x=np.array([[1,2],[3,4]])
print(x)

print('\n用lg.det(x)计算行列式\n',lg.det(x))






'''矩阵的秩'''
I = np.eye(3) # 先创建一个单位阵
print(I)
# [[1. 0. 0.]
# [0. 1. 0.]
# [0. 0. 1.]]
r = np.linalg.matrix_rank(I)
print(r) # 3
I[1, 1] = 0 # 将该元素置为0
print(I)
# [[1. 0. 0.]
# [0. 0. 0.]
# [0. 0. 1.]]
r = np.linalg.matrix_rank(I) # 此时秩变成2
print('\n返回矩阵的秩np.linalg.matrix_rank(I) \n',r) # 2




'''矩阵的迹'''
print('\n方阵的迹就是主对角元素之和。\n')

x = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
print(x)
# [[1 2 3]
# [3 4 5]
# [6 7 8]]
y = np.array([[5, 4, 2], [1, 7, 9], [0, 4, 5]])
print(y)
# [[5 4 2]
# [1 7 9]
# [0 4 5]]
print(np.trace(x)) # A的迹等于A.T的迹
# 13
print(np.trace(np.transpose(x)))
# 13
print(np.trace(x + y)) # 和的迹 等于 迹的和
# 30
print(np.trace(x) + np.trace(y))
# 30




new_matrix=np.array([[1,2,3],[5,6,7],[10,11,12]])
print(new_matrix)

print(np.transpose(new_matrix))
print(new_matrix.T)
print('\nmatrix.T  和 np.transpose(matrix)的效果一样\n')





'''解方程和逆矩阵'''

print('\n逆矩阵（inverse matrix）\n')
print("使用 numpy.linalg.inv(a)")
print('矩阵可逆的充要条件： det(a) != 0 ，或者 a 满秩: det代表行列式不能为0')
A = np.array([[1, -2, 1], [0, 2, -1], [1, 1, -2]])
print(A)
# [[ 1 ‐2 1]
# [ 0 2 ‐1]
# [ 1 1 ‐2]]

# 求A的行列式，不为零则存在逆矩阵
A = np.array([[1, -2, 1], [0, 2, -1], [1, 1, -2]])
print(A)
# [[ 1 ‐2 1]
# [ 0 2 ‐1]
# [ 1 1 ‐2]]
# 求A的行列式，不为零则存在逆矩阵
A_det = np.linalg.det(A)
print(A_det)
# ‐2.9999999999999996
A_inverse = np.linalg.inv(A) # 求A的逆矩阵
print(A_inverse)
# [[ 1.00000000e+00 1.00000000e+00 ‐1.11022302e‐16]
# [ 3.33333333e‐01 1.00000000e+00 ‐3.33333333e‐01]
# [ 6.66666667e‐01 1.00000000e+00 ‐6.66666667e‐01]]
x = np.allclose(np.dot(A, A_inverse), np.eye(3))
print(x) # True
x = np.allclose(np.dot(A_inverse, A), np.eye(3))
print(x) # True
A_companion = A_inverse * A_det # 求A的伴随矩阵
print(A_companion)
# [[‐3.00000000e+00 ‐3.00000000e+00 3.33066907e‐16]
# [‐1.00000000e+00 ‐3.00000000e+00 1.00000000e+00]
# [‐2.00000000e+00 ‐3.00000000e+00 2.00000000e+00]]


'''求解线性方程组'''
'''numpy.linalg.solve(a, b) 求解线性方程组或矩阵方程。'''
# x + 2y + z = 7
# 2x ‐ y + 3z = 7
# 3x + y + 2z =18
import numpy as np
A = np.array([[1, 2, 1], [2, -1, 3], [3, 1, 2]])
b = np.array([7, 7, 18])
x = np.linalg.solve(A, b)
print(x) # [ 7. 1. ‐2.]
x = np.linalg.inv(A).dot(b)
print(x) # [ 7. 1. ‐2.]
y = np.allclose(np.dot(A, x), b)
print(y) # True


