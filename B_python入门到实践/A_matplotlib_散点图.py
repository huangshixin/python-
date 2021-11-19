import matplotlib.pyplot as py

xlabel =[1,2,3,4,5,6]
ylabel =[1,4,9,16,25,36]
#泽瑞的scatter（xlabel，ylabel）
py.xlabel("value",fontsize=14)
py.ylabel("square of value",fontsize=14)
py.scatter(xlabel,ylabel)
py.tick_params(axis='both',which='major',labelsize=14)
py.show()


#自动计算数据
x_value =list(range(1,1001))
y_values = [x**2 for x in x_value]
py.scatter(x_value,y_values,c='red', edgecolors='none',s=40)
py.axis([0,1100,0,1100000])
py.show()