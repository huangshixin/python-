
"""      python 第四章     讲诉如何系统的操作列表    """

#循环遍历列表
""" 语法是 = for 循环名 in 列表名:  """
magicians = ['alice','david','carolina']
""" 列表是一种用[]来表示"""
for cycle_name in magicians:#冒号是告诉python下一条开始执行循环
    print("I can't wait to see your next trick"+"\t"+cycle_name.upper()) #缩进问题 循环语句需要缩进，其它的不需要缩进
# 循环结束的结尾需要对系统进行一些说明
print("\nThank you,everyone.That was a great magic show")
#计算列表的值
print(len(magicians))

#使用range语句  只能打印1~4
for value in range(1,5):
    print(value+1)

#用list做一个列表  将列表中的值变成实际的值
numbers=list(range(1,5))
even_numbers=list(range(2,12,3))
print(numbers)
print("打印从2开始计算_不超过12的_以3为递增的数值")
print(even_numbers)
#定义一个列表，利用循环每次从range函数当中取出一个数字，利用append的方法新增到squres的列表当中当中去
print("\n延申：将一些值计算后存入到系统当中去")
squres = []
for squre in range(2,13,2):
    message = squre**2
    squres.append(message) #添加一个新的值进入列表或者元组当中
print(squres)
print("\n")
#举一反三  python中没有++ 和——
fruits = []
count =0
for fruit in range(3,15):#没有任何提示 每次加三,当然到不了15这点要理解
    information = fruit+3
    fruits.insert(count,information)
    count=count+1 #python不会直接去执行count+1 而是需要一定的语句
print(fruits)

#统计函数 min max sum
print("打印最小值")
print(min(fruits))
print("打印最大值")
print(max(fruits))
print("求和")
print(sum(fruits))

#python 4.4切片原理
"""
补充一下知识：
[:]全局
[:3] 到达第三个
[3：] 不包含第三个，从第三个到结尾
"""
Players = ['charies','martina','florence','eli','huangshixin','dongjm','cxj','oj']
print("数据切片的实际效果"+"\n"+"打印列表的中值的个数")
print(len(Players))
print("切片的[2:7]代表角标为2开始，一个输出到从整个列表看第七个")  #这样切是从3~7 但是角标从2开始
print(Players[2:7]) #切片和range函数很像 不包括最后一个
print("2角标到最后")
print(Players[2:]) #从角标2开始到最后
print("不指明则从0角标开始")
print(Players[:7])#从0开始到最后   Players[:]

#复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:] #从开始到最后

print("My favorite food are :")
print(my_foods)

print("\nMy friend's food are:"+str(friend_foods))#python中的字符串拼接一定要使用str或者其它方式转化成同一类型

#定义一个元组
""" 元组是一种()"""
print("元组是一种用括号表示的东西")
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
print("\n")
#测试元组
number_message = (1,2,3,4,4,5,6,6,7,7,7,8,9,9,9,0,0,)
print("打印元组中的值")
print(len(number_message))
for number_messages in number_message:
    print(number_messages)#索引number_messages