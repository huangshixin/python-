import numpy as np

a = np.arrar([True,False,True])

#any表示，当a中存在一个True时候，返回True
print(np.any(a)) 

#all
#表示，a中必须全为True，才能返回True
print(np.all(a)) 


#numpy运算支持广播运算

1、支持numpy的array与一个【数】进行比较，而且【返回】一个数组
#查询数组中大于10的数，并返回一个列表，之后再调用any（）判断是否存在至少一个大于10的
(arr>10).any()


#比如一个数组加上一个数
arr = np.array([1,2,3,4,5])
b = 5
#arr+b ===【6，7，8，9，10】
'''
由于b是一维，那么再做运算的时候，numpy会对b的维度进行【广播】，以达到arr的维度，而缺失值使用5来填充
'''
