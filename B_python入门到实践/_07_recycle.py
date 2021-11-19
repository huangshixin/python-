""" 7章 用户输入和while循环"""
# input在控制台中的使用场景
# int（）将输入的值转化为int型
# 如何在系统自动的结束
# break 和continue在循环当中的区别
# while 处理字典和列表

#input() 就是重复回答你一些问题
print("input()方法使用：目的是从control table 传输一些值到系统而使得系统暂时的停止")
#字符串类型
message = input("Tell me something,I will repeat it back to you :")
print(message)

#拼接字符串, 字符串可以放在变量中被打印出来(实际上这input就是类似于提示词)
print("input函数输出的是一种字符串")
name =input("please enter your name:")#input的结果应该是字符串
print("Hello,"+name+"!")
access = "I want to talk you something about my hometown"
name +=","+access#
information = input(name+".")
print(information+"happy everday"+"\n")

#使用int函数
""" int 需要配合input使用"""
print("int函数是用来将输入的值转化为int型的值")
print("Honey,I want to eat hot-pot with you tonight,could you agree it?")
mess_age = input("how many people?")
values = int(mess_age)
print("ok")
if values == 2:
    print("Are you still love me?")
else:
    print("I have been hated you . are you  human?")
    print("Oh,my godness,you have other's women in your heart.")
    #oh,my god 这是一种惊讶但是是很差的事情
    #oh,my godness, 这个比较文明

#取余运算符 %
value = 4%3
print("Guess what this number")
print(value)


#while循环简介
# #for循环对待字典，列表，元组   while集合
current = 1
while current <= 5:
    print(current)
   # print("I love your story about Chinese historic culture")
    current +=1 #每次在加一

#设计一个语句使得程序自己结束
print("Hello again\n")
messages = input("please enter a number:")
value = int(messages)
if value ==3:
    print("The program over")
else:
    values = input("Please enter an novel string")
    print("The string is :"+values)

#break 和 continue的使用
friends = ['chenxingjie','oujie','liuchengfeng','HC','djm','dlm','lsh','dxt','cys','rjj','lqf','lwj']

length = len(friends)
if length == 12:
    print("true")
else:
    print("False")
count = 1
for friend in friends:
    while count <= length:
        if friend == 'djm':
            print("这是个坑狗")
            continue
        elif friend =='lwj':
            print("Scan over")
        else:
            break
        count += 1

for friend in friends:
    if friend == 'djm':
        print(friend)
        print("这是个坑狗")
        continue
    elif friend == 'lwj':
        print(friend)
        print("这个更坑")
        break
print("THE PROGRAM OVER")

# while 处理字典和列表
"""
 功能：希望把一个列表中新添加但是为验证的名单加到另一个；列表当中
    Questions:如何确定A列表当中的值B列表当中没有
            如何添加到新的列表当中去
"""
friends = ['chenxingjie','oujie','liuchengfeng','HC','djm','dlm','lsh','dxt','cys','rjj','lqf','lwj']
friends_2 = ['chenxingjie']
print("打印列表1")
print(friends)
print("打印列表2")
print(friends_2)
for friend in friends:
    if friend not in friends_2:
        friends_2.append(friend)
    elif friend == 'chenxingjie':
        friends_2.remove(friend)
    elif friend == 'rjj':
        friends_2.append(friend)
        break#证明了一个问题 列表是无序的
print("再次打印列表2")
print(friends_2)


#处理字典
kids = {
    'name_1':'djm',
    'name_2':'lwj',
    'name_3':'hc'
        }
