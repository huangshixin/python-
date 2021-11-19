"""
第十五章
    生成数据
    安装步骤：p286
    https://pypi.org/project/matplotlib/#files 下载matplotilb
    python -m pip install --user filename.whl
"""


from random import matplotlib as plt

#绘制简单的折线图
"""因为系统默认从x=0出发，因此为了校准图形。我们可以同时给他传入输入值和输出值"""
squares_output = [1,4,9,16,25]
squares = [1,2,3,4,5]
#设置线条的粗细
plt.plot(squares,squares_output,linewidth=5)

#title给表格设置名字，xlabel是x坐标，ylabel是y坐标
plt.title("square number" , fontsize=24)
plt.xlabel("value",fontsize =24)#x轴的名称
plt.ylabel("square of value",fontsize = 24)#y轴的名称

#设置刻度标记的大小（途中x或作y的刻度的表示）
plt.tick_params(axis='both',labelsize =14)
plt.show()