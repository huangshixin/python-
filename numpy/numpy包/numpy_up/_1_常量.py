#常量
import numpy as np
"""
空值是无法比较的

isnan(x)#判断x是否为空 返回的值是你输入的值    nan==空值
count_nonzero(y)#判断传入的列表y是否为空  如果为空自动加1·(相当于计算空值个数）
"""
# 1_numpay.nan 表示空值
print(np.nan ==np.nan)#空值是无法比较的
print(np.nan !=np.nan)#true
x=np.array([1,1,8,np.nan,10,np.nan])
print(x)
y=np.isnan(x)#判断x是否为空 返回的值是你输入的值    nan==空值
print(y)
'计算列表或者元组中空值的个数'
z=np.count_nonzero(y)#判断传入的y是否为空  如果为空自动加1·
print(z)





#numpy.inf 表示无穷大
#Inf = inf = infty = Infinity = PIN
pretend_inf =np.inf
print(pretend_inf)



#numpy.pi
pi = 3.1415926535897932384626433


#numpy.e
e = 2.71828182845904523536028747135266249775724709369995



'''是否想知道数组的维度
使用array.ndim看维度
使用type（）


'''
#常用的方法
'''
1.np.random.random()函数参数
np.random.random((1000, 20))生成一个矩阵（1000，20）   每个值都是从0-1中随机。



2.numpy.random.rand()函数用法
numpy.random.rand(d0, d1, ..., dn)：生成一个[0,1)之间的随机浮点数或N维浮点数组。

 

3.numpy.random.randn()函数用法： 
numpy.random.randn(d0, d1, ..., dn)：生成一个浮点数或N维浮点数组，取数范围：正态分布的随机样本数。

 

4.numpy.random.standard_normal()函数用法
numpy.random.standard_normal(size=None)：生产一个浮点数或N维浮点数组，取数范围：标准正态分布随机样本

 

5.numpy.random.randint()函数用法：
numpy.random.randint(low, high=None, size=None, dtype='l')：生成一个整数或N维整数数组，取数范围：若high不为None时，取[low,high)之间随机整数，否则取值[0,low)之间随机整数。

 

6.numpy.random.random_integers()函数用法：

numpy.random.random_integers(low, high=None, size=None)：
生成一个整数或一个N维整数数组，取值范围：若high不为None，则取[low,high]之间随机整数，否则取[1,low]之间随机整数。

 

7.numpy.random.random_sample()函数用法

numpy.random.random_sample(size=None)：
生成一个[0,1)之间随机浮点数或N维浮点数组。

 

8.numpy.random.choice(）函数用法
numpy.random.choice(a, size=None, replace=True, p=None)：从序列中获取元素，若a为整数，******元素取值为np.range(a)中随机数******；若a为数组，取值为a数组元素中随机元素。

 

9.numpy.random.shuffle()函数用法
numpy.random.shuffle(x)：对X进行重排序，如果X为多维数组，只沿第一条轴洗牌，输出为None。如果是二维数组则是按照每个模块打乱  但是他把原来的数组打乱了 不好

 

10.numpy.random.permutation()函数用法
numpy.random.permutation(x)：与numpy.random.shuffle(x)函数功能相同，两者区别：peumutation(x)不会修改X的顺序。



11、ndarry必须是同一种类型  而list不一定是同一种类型
#ndarray可对维数不同的矢量进行广播计算



12
np.ndim(x)看你是哪一种维度的   比如二维数组
type（x）看你的类型 
dtype(x)看 属性
mean求均值
sum求和
argmax返回最大值的角标index
argmin 返回最小值的角标
nonzero返回非0的角标
reshape改



13 
array转化为数组形式
list转化为list
ravel转为列表
'''