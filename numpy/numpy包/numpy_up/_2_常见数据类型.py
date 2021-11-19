import numpy as np
import random
import time


#基本的数据类型
"""
bool_ = bool8 8位 布尔类型
int8 = byte 8位 整型
int16 = short 16位 整型·
int32 = intc 32位 整型
int_ = int64 = long = int0 = intp 64位 整型
uint8 = ubyte 8位 无符号整型
uint16 = ushort 16位 无符号整型
uint32 = uintc 32位 无符号整型
uint64 = uintp = uint0 = uint 64位 无符号整型
float16 = half 16位 浮点型
float32 = single 32位 浮点型
float_ = float64 = double 64位 浮点型
str_ = unicode_ = str0 = unicode Unicode 字符串
datetime64 日期时间类型
timedelta64 表示两个时间之间的间隔

"""






#numpy 的数值类型实际上是 dtype 对象的实数值
class dtype(object):
    def __init__(self,obj,align=False,copy=False):
        pass

type_a =np.dtype('b')
print(type_a)  # <class 'numpy.bool_'>
print(type_a.itemsize)#返回数组中每个字符的长度

type_list = ['b','i','u1','f','c','m','M','O','S','U','V']
type_print=[]
for i in range(len(type_list)):
    data = np.dtype(type_list[i])
    type_print.append(data)
print(type_print)
"""
b boolean 'b1'
i signed integer 'i1', 'i2', 'i4', 'i8'
u unsigned integer 'u1', 'u2' ,'u4' ,'u8'
f floating-point 'f2', 'f4', 'f8'
c complex floating-point 
m timedelta64 表示两个时间之间的间隔
M datetime64 日期时间类型
O object 
S (byte-)string S3表示长度为3的字符串
U Unicode Unicode 字符串
V void 
每
"""





                                                    #time
#在 numpy 中，我们很方便的将字符串转换成时间日期类型 datetime64 （ datetime 已被 python 包含的日期时间库所占用）
"""
1. 1秒 = 1000 毫秒（milliseconds） 2. 1毫秒 = 1000 微秒（microseconds）
"""
#2020-12-14 是精确到   日 day
date_a = np.datetime64('2020-12-14') #从字符串创建 datetime64 类型时，默认情况下，numpy 会根据字符串自动选择对应的单位。
print("xxxxxx")
print(date_a,date_a.dtype) #2020-12-14 datetime64[D]
#以下是精确到 月 month
date_month = np.datetime64('2020-12')
print(date_month,date_month.dtype)#2020-12 datetime64[M]
#同理
"""
a = np.datetime64('2020-03-08 20:00:05') print(a, a.dtype)  # 2020-03-08T20:00:05 datetime64[s]
a = np.datetime64('2020-03-08 20:00') print(a, a.dtype)  # 2020-03-08T20:00 datetime64[m]
a = np.datetime64('2020-03-08 20') print(a, a.dtype)  # 2020-03-08T20 datetime64[h]
"""
#从字符串创建 datetime64 类型时，可以强制指定使用的单位。
date_as=np.datetime64('2020-12-14','Y')#强制指定使用的单位
print(date_as,date_as.dtype)
"""
，2019-03 和 2019-03-01 所表示的其实是同一个时间。 事实上，如果两个 datetime64 对象具有不同的单位，它们可能仍然代表相同的时刻。并且从较大的单位（如月份）转换为较小的单位（如天
数）是安全的
print(np.datetime64('2020-03') == np.datetime64('2020-03-01'))  # True 
print(np.datetime64('2020-03') == np.datetime64('2020-03-02'))  #False

"""

#构建datetime64的数组时候
array_a =np.array(['2020-01','2020-02','2020-03','2020-04','2020-04','2020-05-01 20:00'],dtype='datetime64')
print(array_a,array_a.dtype)
