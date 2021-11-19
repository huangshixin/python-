#绘制简单的折线图
import matplotlib.pyplot as plt
input_value = [1,2,3,4,5]
square =[1,4,9,16,25]

#修改标签文字和线条粗细  wideth=15,加上input_value=是为了去校验
plt.plot(input_value,square,linewidth=5)


#设置标题名字和文字的大小 fontsize=24
plt.title("this is a curb",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value",fontsize=24)


#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)

plt.show()


