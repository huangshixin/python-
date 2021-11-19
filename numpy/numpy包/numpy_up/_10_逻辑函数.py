#逻辑函数

import numpy as np

"""
真值测试
1. numpy.all(a, axis=None, out=None, keepdims=np._NoValue) 
2. numpy.any(a, axis=None, out=None, keepdims=np._NoValue) 
numpy.isnan(x, *args, **kwargs) Test element-wise for NaN and return result as a boolean array.
all 要求所有元素相同
any 一部分元素相同就行
isnan 判断是否为空
"""
a = np.array([0, 4, 5])
b = np.copy(a)
print(np.all(a == b)) # True
print(np.any(a == b)) # True
b[0] = 1
print(np.all(a == b)) # False
print(np.any(a == b)) # True
print(np.all([1.0, np.nan])) # True
print(np.any([1.0, np.nan])) # True
a = np.eye(3)#对角线矩阵
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
print(np.all(a, axis=0)) # [False False False]
print(np.any(a, axis=0)) # [ True True True]

"""判断是否为空"""
a=np.array([1,2,np.nan])
print(np.isnan(a))
#[False False True]


"""逻辑运算
 numpy.logical_not(x, *args, **kwargs) Compute the truth value of NOT x element-wise.
2. numpy.logical_and(x1, x2, *args, **kwargs) Compute the truth value of x1 AND x2 element-wise.
3. numpy.logical_or(x1, x2, *args, **kwargs) Compute the truth value of x1 OR x2 element-wise.
4. numpy.logical_xor(x1, x2, *args, **kwargs) Compute the truth value of x1 XOR x2, element-wise.
"""


#逻辑非logical_not
"""
把真的变假的  假的变真的  
print(np.logical_not(True))    False
print(np.logical_not(False))   True
0 某人是假
非0 默认是真
print(np.logical_not([0,2,3,4,5,0,-1]))
[ True False False False False  True False]
"""
print(np.logical_not(3))
# False
print(np.logical_not([True, False, 0, 1]))
# [False True True False]
x = np.arange(5)
print(np.logical_not(x < 3))
# [False False False True True]

"""【例】计算x1 AND x2元素的真值。"""
print(np.logical_and(True, False))
# False
print(np.logical_and([True, False], [True, False]))
# [ True False]
print(np.logical_and(x > 1, x < 4))
# [False False True True False]
"""【例】逐元素计算x1 OR x2的真值。"""
print(np.logical_or(True, False))
# True
print(np.logical_or([True, False], [False, False]))
# [ True False]
print(np.logical_or(x < 1, x > 3))
# [ True False False False True]
"""【例】计算x1 XOR x2的真值，按元素计算。  异或"""
print(np.logical_xor(True, False))
# True
print(np.logical_xor([True, True, False, False], [True, False, True, False]))
# [False True True False]
print(np.logical_xor(x < 1, x > 3))
# [ True False False False True]
print(np.logical_xor(0, np.eye(2)))
# [[ True False]
# [False True]]



"""
对照  返回Boolean值
greater比大小
1、判断是否x1>x2:   numpy.greater(x1, x2, *args, **kwargs) 
2. 判断是否x1>=x2: numpy.greater_equal(x1, x2, *args, **kwargs) 

判断是否相等
3. numpy.equal(x1, x2, *args, **kwargs) Return (x1 == x2) element-wise.
4. numpy.not_equal(x1, x2, *args, **kwargs) Return (x1 != x2) element-wise.

less比小
一个是小于 一个是小于等于
5. numpy.less(x1, x2, *args, **kwargs) Return the truth value of (x1 < x2) element-wise.
6. numpy.less_equal(x1, x2, *args, **kwargs) Return the truth value of (x1 =< x2) element-wise.

"""
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = x > 2
print(y)
print(np.greater(x, 2))
# [False False True True True True True True]
y = x >= 2
print(y)
print(np.greater_equal(x, 2))
# [False True True True True True True True]
y = x == 2
print(y)
print(np.equal(x, 2))
# [False True False False False False False False]
y = x != 2
print(y)
print(np.not_equal(x, 2))
# [ True False True True True True True True]
y = x < 2
print(y)
print(np.less(x, 2))
# [ True False False False False False False False]
y = x <= 2
print(y)
print(np.less_equal(x, 2))
# [ True True False False False False False False]
"""二维情况下比较"""
x = np.array([[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])
y = x > 20
print(y)
print(np.greater(x, 20))
# [[False False False False False]
# [False False False False False]
# [ True True True True True]
# [ True True True True True]
# [ True True True True True]]
y = x >= 20
print(y)
print(np.greater_equal(x, 20))
# [[False False False False False]
# [False False False False True]
# [ True True True True True]
# [ True True True True True]
# [ True True True True True]]
y = x == 20
print(y)
print(np.equal(x, 20))
# [[False False False False False]
# [False False False False True]
# [False False False False False]
# [False False False False False]
# [False False False False False]]
y = x != 20
print(y)
print(np.not_equal(x, 20))
# [[ True True True True True]
# [ True True True True False]
# [ True True True True True]
# [ True True True True True]
# [ True True True True True]]
y = x < 20
print(y)
print(np.less(x, 20))
# [[ True True True True True]
# [ True True True True False]
# [False False False False False]
# [False False False False False]
# [False False False False False]]
y = x <= 20
print(y)
print(np.less_equal(x, 20))
# [[ True True True True True]
# [ True True True True True]
# [False False False False False]
# [False False False False False]
# [False False False False False]]

np.random.seed(20200611)
x = np.array([[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])
y = np.random.randint(10, 40, [5, 5])
print(y)
# [[32 28 31 33 37]
# [23 37 37 30 29]
# [32 24 10 33 15]
# [27 17 10 36 16]
# [25 32 23 39 34]]
z = x > y
print(z)
print(np.greater(x, y))
# [[False False False False False]
# [False False False False False]
# [False False True False True]
# [False True True False True]
# [ True False True False True]]
z = x >= y
print(z)
print(np.greater_equal(x, y))
# [[False False False False False]
# [False False False False False]
# [False False True False True]
# [False True True False True]
# [ True True True False True]]
z = x == y
print(z)
print(np.equal(x, y))
# [[False False False False False]
# [False False False False False]
# [False False False False False]
# [False False False False False]
# [False True False False False]]
z = x != y
print(z)
print(np.not_equal(x, y))
# [[ True True True True True]
# [ True True True True True]
# [ True True True True True]
# [ True True True True True]
# [ True False True True True]]
z = x < y
print(z)
print(np.less(x, y))
# [[ True True True True True]
# [ True True True True True]
# [ True True False True False]
# [ True False False True False]
# [False False False True False]]
z = x <= y
print(z)
print(np.less_equal(x, y))
# [[ True True True True True]
# [ True True True True True]
# [ True True False True False]
# [ True False False True False]
# [False True False True False]]


import numpy as np
x = np.array([[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])
np.random.seed(20200611)
y = np.random.randint(10, 50, 5)
print(y)
# [32 37 30 24 10]
z = x > y

print(z)
print(np.greater(x, y))
# [[False False False False True]
# [False False False False True]
# [False False False False True]
# [False False False True True]
# [False False True True True]]
z = x >= y
print(z)
print(np.greater_equal(x, y))
# [[False False False False True]
# [False False False False True]
# [False False False True True]
# [False False False True True]
# [False False True True True]]
z = x == y
print(z)
print(np.equal(x, y))
# [[False False False False False]
# [False False False False False]
# [False False False True False]
# [False False False False False]
# [False False False False False]]
z = x != y
print(z)
print(np.not_equal(x, y))
# [[ True True True True True]
# [ True True True True True]
# [ True True True False True]
# [ True True True True True]
# [ True True True True True]]
z = x < y
print(z)
print(np.less(x, y))
# [[ True True True True False]
# [ True True True True False]
# [ True True True False False]
# [ True True True False False]
# [ True True False False False]]
z = x <= y
print(z)
print(np.less_equal(x, y))
# [[ True True True True False]
# [ True True True True False]
# [ True True True True False]
# [ True True True False False]
# [ True True False False False]]


"""
1. numpy.isclose(a, b, rtol=1.e-5, atol=1.e-8, equal_nan=False)
2. numpy.allclose(a, b, rtol=1.e-5, atol=1.e-8, equal_nan=False) 
"""
#83




















