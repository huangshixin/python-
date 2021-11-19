from matplotlib import pyplot as plt
import random
#i/2 for i in range(4,49)
"""
列表的知识：
[i/2 for i in range(4,49)]  把遍历出来的数据除于2 然后存放到列表当中去  ,你可以理解为range函数只是为了输出一个次数 之后i/2是我们真正的操作

abc=[random.randint(20,35) for i in range(10)]
[35, 20, 30, 27, 25, 27, 20, 33, 34, 26] 结果不一定

min max 方法

列表当中的切片：
假定   _xtick_labels  是列表
_xtick_labels[::3]  以3为"步伐"进行切片
"""
x= range(0,120)
y= [random.randint(20,35) for i in range(120)]

#设置图片的大小
fig =plt.figure(figsize=(20,8),dpi=80)

#x绘图
plt.plot(x,y)

# _xtick_labels = [i/2 for i in range(4,49)]
# plt.xticks(_xtick_labels[::3])
# plt.yticks(range(min(y),max(y)+1))


#展示图片
plt.show()