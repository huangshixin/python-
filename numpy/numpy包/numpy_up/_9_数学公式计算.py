def ma():
    pass
"""
数学公式一：
1.加法 numpy.add(x1, x2, *args, **kwargs) Add arguments element-wise.
2.减法numpy.subtract(x1, x2, *args, **kwargs) Subtract arguments element-wise.
3.乘法numpy.multiply(x1, x2, *args, **kwargs) Multiply arguments element-wise.
4.除法 numpy.divide(x1, x2, *args, **kwargs) Returns a true division of the inputs, element-wise.
5.输出小于或者等于的最大整数 【eg 1.3  则结果就是1】 numpy.floor_divide(x1, x2, *args, **kwargs) Return the largest integer smaller or equal to the division of the inputs.
6.开平方numpy.power(x1, x2, *args, **kwargs) First array elements raised to powers from second array, element-wise.
"""

import numpy as np

"""加法"""
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y=x+1
print(y)
print(np.add(x,1))#相当于每个位置加了个1
#[2 3 4 5 6 7 8 9]

"""减法"""
y = x - 1
print(y)
print(np.subtract(x, 1))

"""乘法"""
y = x * 2
print(y)
print(np.multiply(x, 2))


"""除法"""
y = x / 2
print(y)
print(np.divide(x, 2))

"""赋值"""
y = x // 2
print(y)
print(np.floor_divide(x, 2))
# [0 1 1 2 2 3 3 4]


"""头上角标"""
y = x ** 2 #x^2
print(y)
print(np.power(x, 2))
# [ 1 4 9 16 25 36 49 64]


""""二维数组"""

x = np.array([[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])
y = np.arange(1, 6)
print(y)
# [1 2 3 4 5]
z = x + y
print(z)
print(np.add(x, y))
# [[12 14 16 18 20]
# [17 19 21 23 25]
# [22 24 26 28 30]
# [27 29 31 33 35]
# [32 34 36 38 40]]

"""减法"""
z = x - y
print(z)
print(np.subtract(x, y))
# [[10 10 10 10 10]
# [15 15 15 15 15]
# [20 20 20 20 20]
# [25 25 25 25 25]
# [30 30 30 30 30]]
z = x * y
print(z)
print(np.multiply(x, y))
# [[ 11 24 39 56 75]
# [ 16 34 54 76 100]
# [ 21 44 69 96 125]
# [ 26 54 84 116 150]
# [ 31 64 99 136 175]]
z = x / y
print(z)
print(np.divide(x, y))
# [[11. 6. 4.33333333 3.5 3. ]
# [16. 8.5 6. 4.75 4. ]
# [21. 11. 7.66666667 6. 5. ]
# [26. 13.5 9.33333333 7.25 6. ]
# [31. 16. 11. 8.5 7. ]]
z = x // y
print(z)
print(np.floor_divide(x, y))
# [[11 6 4 3 3]
# [16 8 6 4 4]
# [21 11 7 6 5]
# [26 13 9 7 6]
# [31 16 11 8 7]]
z = x ** np.full([1, 5], 2)
print(z)
print(np.power(x, np.full([5, 5], 2)))
# [[ 121 144 169 196 225]
# [ 256 289 324 361 400]
# [ 441 484 529 576 625]
# [ 676 729 784 841 900]
# [ 961 1024 1089 1156 1225]]


"""
数学公式二：
1、np.sqrt 开根号   ==np.power(x,0.5)
2.square 平方（正方形 方的） ==np.power(x,2) 开平方 x**2

"""
import numpy as np
x = np.arange(1, 5)
print(x) # [1 2 3 4]
y = np.sqrt(x)
print(y)
# [1. 1.41421356 1.73205081 2. ]
print(np.power(x, 0.5))
# [1. 1.41421356 1.73205081 2. ]
y = np.square(x)
print(y)
# [ 1 4 9 16]
print(np.power(x, 2))
# [ 1 4 9 16]


"""
数学公式三：
三角函数：
sin
cos
tan
arcsin
arccos
arctan
"""
#linspace 是计算等差数列的
# x = np.linspace(start=0, stop=np.pi / 2, num=10)
# print(x)
# # [0. 0.17453293 0.34906585 0.52359878 0.6981317 0.87266463
# # 1.04719755 1.22173048 1.3962634 1.57079633]
"""这是一个等差数列列表"""
list_x=np.linspace(0,np.multiply(np.pi,0.5),3)

print("打印sinx在0-2pi之间的效果：",np.sin(list_x))
print("打印cosx在0-2pi之间的效果：",np.cos(list_x))
print("打印tanx在0-2pi之间的效果：",np.tan(list_x))
print("打印arcsinx在0-2pi之间的效果：",np.arcsin((list_x)))
print("打印arccosx在0-2pi之间的效果：",np.arccos(list_x))
print("打印arctanx在0-2pi之间的效果：",np.arctan(list_x))



"""
数学公式四：
指数和对数
exp
log
exp2
log2
log10

"""
import numpy as np
x = np.arange(1, 5)
print(x)
# [1 2 3 4]
y = np.exp(x)
print(y)
# [ 2.71828183 7.3890561 20.08553692 54.59815003]
z = np.log(y)
print(z)
# [1. 2. 3. 4.]


"""
数学公式五：
sum
如果不标注axis
则它是通过地址角标递增的方式进行累计求和
如果你标注axis（当然指的是二维以上的数组）
axis=0，代表从纵轴开始求和
axis=1 ，代表从横轴开始求和
"""

x = np.array(
[[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])
y=np.sum(x)
print(y)# 575
y = np.sum(x, axis=0)
print(y) # [105 110 115 120 125]
y = np.sum(x, axis=1)
print(y) # [ 65 90 115 140 165]


"""
numpy.cumsum
聚合函数 是指对一组值（比如一个数组）进行操作，返回一个单一值作为结果的函数。因而，求数组所有元素之和的函数就是聚合函
数。 ndarray 类实现了多个这样的函数。


这个作用就是把某列或者某行进行聚合
如果是单个列表或者数组，则 根据角标递增，【把前一个的求和加到后一个上）
如果有axis
axis=0，代表从纵轴开始求和，不过规则还是把该行或者列的求和结果加到下一列或者行
axis=1 ，代表从横轴开始求和
"""
x = np.array(
[[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])
y = np.cumsum(x)
print(y)
# [ 11 23 36 50 65 81 98 116 135 155 176 198 221 245 270 296 323 351
# 380 410 441 473 506 540 575]
"""

"""
y = np.cumsum(x, axis=0)
print(y)
# [[ 11 12 13 14 15]
# [ 27 29 31 33 35]
# [ 48 51 54 57 60]
# [ 74 78 82 86 90]
# [105 110 115 120 125]]
y = np.cumsum(x, axis=1)
print(y)
# [[ 11 23 36 50 65]
# [ 16 33 51 70 90]
# [ 21 43 66 90 115]
# [ 26 53 81 110 140]
# [ 31 63 96 130 165]]

"""
数学公式六：
numpy.prod乘积
numpy.prod(a[, axis=None, dtype=None, out=None, …]) Return the product of array elements over a given axis.
1 这个的计算如果直接调用prod则是把返回一个数 （一个经过累计求和的数)
2、如果有axis
则思考 按照 列或者行求和计算（对应位置
x = np.array([[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])

axis=0
 [2978976 3877632 4972968 6294624 7875000]

axis=1
 [ 360360 1860480 6375600 17100720 38955840]


 
numpy.cumprod 累乘
numpy.cumprod(a, axis=None, dtype=None, out=None) Return the cumulative product of elements along a given axis.

x = np.array([[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])

cumprod（x）
 ################# 字面意思就是 把该乘积的结果 连接到下一个值上#################
 [ 11 132 1716 24024 360360 5765760
# 98017920 1764322560 -837609728 427674624 391232512 17180672
# 395155456 893796352 870072320 1147043840 905412608 -418250752
# 755630080 1194065920 -1638662144 -897581056 444596224 -2063597568
# 788529152]

axis=0
# [[ 11 12 13 14 15]
# [ 176 204 234 266 300]
# [ 3696 4488 5382 6384 7500]
# [ 96096 121176 150696 185136 225000]
# [2978976 3877632 4972968 6294624 7875000]]


axis=1
# [[ 11 132 1716 24024 360360]
# [ 16 272 4896 93024 1860480]
# [ 21 462 10626 255024 6375600]
# [ 26 702 19656 570024 17100720]
# [ 31 992 32736 1113024 38955840]]

"""

x = np.array([[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])
y = np.prod(x)
print(np.prod(x))
x=np.arange(1,3)
print(np.prod(x))#1*2
y = np.prod(x, axis=0)
print(y)
# [2978976 3877632 4972968 6294624 7875000]
y = np.prod(x, axis=1)
print(y)
# [ 360360 1860480 6375600 17100720 38955840]

x = np.array([[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])
y = np.cumprod(x)
print(y)
# [ 11 132 1716 24024 360360 5765760
# 98017920 1764322560 -837609728 427674624 391232512 17180672
# 395155456 893796352 870072320 1147043840 905412608 -418250752
# 755630080 1194065920 -1638662144 -897581056 444596224 -2063597568
# 788529152]
y = np.cumprod(x, axis=0)
print(y)
# [[ 11 12 13 14 15]
# [ 176 204 234 266 300]
# [ 3696 4488 5382 6384 7500]
# [ 96096 121176 150696 185136 225000]
# [2978976 3877632 4972968 6294624 7875000]]
y = np.cumprod(x, axis=1)
print(y)
# [[ 11 132 1716 24024 360360]
# [ 16 272 4896 93024 1860480]
# [ 21 462 10626 255024 6375600]
# [ 26 702 19656 570024 17100720]
# [ 31 992 32736 1113024 38955840]]



"""
数学公式七： 差值
 numpy.diff(a, n=1, axis=-1, prepend=np._NoValue, append=np._NoValue) Calculate the n-th discrete difference along the given
axis.
a. a：输入矩阵
b. n：可选，代表要执行几次差值
c. axis：默认是最后一个
"""
A = np.arange(2, 14).reshape((3, 4))
A[1, 1] = 8 #==A[1][1]
print(A)
# [[ 2 3 4 5]
# [ 6 8 8 9]
# [10 11 12 13]]
print(np.diff(A))
# [[1 1 1]
# [2 0 1]
# [1 1 1]]

print(np.diff(A, axis=0))#按照列相减 eg：最后一列减去倒二列（下减去上）
# [[4 5 4 4]
# [4 3 4 4]]
print(np.diff(A, axis=1))#按照行相减 eg：右边减去左边

"""
数学公式8：

numpy.around 四舍五入 
np.random.rand(3, 3)生成一个3x3的矩阵，矩阵中的值是0-1之间的
np.random.rand(3)生成一个列表 中的值是0-1之间

"""
x = np.random.rand(3, 3) * 10
print(x)
# [[6.59144457 3.78566113 8.15321227]
# [1.68241475 3.78753332 7.68886328]
# [2.84255822 9.58106727 7.86678037]]
y = np.around(x)

x = np.random.rand(3, 3) * 10
print(y)
# [[ 7. 4. 8.]
# [ 2. 4. 8.]
# [ 3. 10. 8.]]
y = np.around(x, decimals=2)
print(y)
# [[6.59 3.79 8.15]
# [1.68 3.79 7.69]
# [2.84 9.58 7.87]]


print(np.ceil(x))
# [[1. 2. 5.]
# [8. 6. 3.]
# [9. 9. 6.]]

y = np.floor(x)
print(y)
# [[0. 1. 4.]
# [7. 5. 2.]
# [8. 8. 5.]]


"""
数学公式九：
numpy.clip 裁剪
numpy.absolute 绝对值
numpy.abs 
numpy.sign 返回数字符号的逐元素指示
"""
x = np.array([[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25],
[26, 27, 28, 29, 30],
[31, 32, 33, 34, 35]])
y = np.clip(x, a_min=20, a_max=30)
print(y)
# [[20 20 20 20 20]
# [20 20 20 20 20]
# [21 22 23 24 25]
# [26 27 28 29 30]
# [30 30 30 30 30]]

x = np.arange(-5, 5)
print(x)
# [-5 -4 -3 -2 -1 0 1 2 3 4]
y = np.abs(x)
print(y)
# [5 4 3 2 1 0 1 2 3 4]
y = np.absolute(x)
print(y)
# [5 4 3 2 1 0 1 2 3 4]
x = np.arange(-5, 5)
print(x)
#[-5 -4 -3 -2 -1 0 1 2 3 4]
print(np.sign(x))
#[-1 -1 -1 -1 -1 0 1 1 1 1]

#74
