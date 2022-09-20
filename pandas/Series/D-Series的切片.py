import numpy as np
import pandas as pd
import matplotlib as mpl


#以下默认s是Serise的形式


#如果是使用隐式索引进行切片
s[1:3]---【左闭右开】

#如果使用显式索引
s['licy':'mery']----【左右封闭】------只有显式索引这种情况是 【【【左右封闭】】】


#如果使用loc访问
s.loc['licy':'mery']---【左闭右闭】

#使用iloc
s.iloc[1:3]



