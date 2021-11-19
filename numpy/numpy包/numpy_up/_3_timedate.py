
import numpy as np
import datetime
#datetime

"""时间做差"""
#timedelta64 表示两个 datetime64 之间的差
a = np.datetime64('2020-03-08') - np.datetime64('2020-03-07')
b = np.datetime64('2020-03-08') - np.datetime64('202-03-07 08:00')
c = np.datetime64('2020-03-08') - np.datetime64('2020-03-07 23:00', 'D')
print(a, a.dtype)  # 1 days timedelta64[D]
print(b, b.dtype)  # 956178240 minutes timedelta64[m]
print(c, c.dtype)  # 1 days timedelta64[D
#tips
"""
1、在datetime64的方法内可以指定输出的时间的类型
a = np.datetime64('2020-03') + np.timedelta64(20, 'D') 
b = np.datetime64('2020-06-15 00:00') + np.timedelta64(12, 'h') 
print(a, a.dtype)  # 2020-03-21 datetime64[D] 
print(b, b.dtype)  # 2020-06-15T12:00 datetime64[m]
"""

time_a = np.timedelta64(1,'Y')#表示几年
time_b = np.timedelta64(time_a,'M')
print(time_a)# 1years
print(time_b)# 12months
print('\n')
time_c = np.timedelta64(1,'h')
time_d = np.timedelta64(time_c,'s')#seconds or minutes[ˈmɪnɪts]
print(time_c)
print(time_d)
print('\n')
#时间加法
a = np.timedelta64(1, 'Y')
b = np.timedelta64(6, 'M')
c = np.timedelta64(1, 'W')
d = np.timedelta64(1, 'D')
e = np.timedelta64(10, 'D')
print(a)  # 1 years
print(b)  # 6 months
print(a + b)  # 18 months
print(a - b)  # 6 months
print(2 * a)  # 2 years
print(a / b)  # 2.0
print(c / d)  # 7.0
print(c % e)  # 7 days


#时间类型转换
dt = datetime.datetime(year=2020, month=6, day=1, hour=20, minute=5, second=30)
dt64 = np.datetime64(dt, 's')
print(dt64, dt64.dtype) # 2020-06-01T20:05:30 datetime64[s]
dt2 = dt64.astype(datetime.datetime)
print(dt2, type(dt2)) # 2020-06-01 20:05:30 <class 'datetime.datetime'>




#datetime64的应用
