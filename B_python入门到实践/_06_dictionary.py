#direction 方向 方位 趋势
#dictionary 字典

""" 语法     字典名 = {'':字典值,'':}"""
""" 回顾一下列表和元组  column_name=[]/ group_name = ()"""
alien_0 ={'color':'green' , 'points': 5}#'color':'green'  这是一种键值对的形式    key--value
print(alien_0['color']) #无论你是列表/元组/字典 如果通过角标访问 具体的某个值 都需要[]
print(alien_0['points'])
#拼接键值对
message = alien_0['color'] #'' 这个在python当中只是一个未定义类型的值罢了
print("this is worst a color :"+"\t"+str(message)+".")
print("\n")

#如何添加键值对
humans = {}
humans['color'] ='yellow'
humans['quantity'] ='5'
humans['black_people'] ='hosptile' #nigger 【尼哥】 niger【nai dgr】乃嘴
humans['color'] ='pink'
print("打印字典")#字典的数据不分前后
print(humans)
print("\n")

#修改键值对中的数据
humans['color'] ='red'
print(humans)

#删除键值对 del
print("新增一个键值对并且删除案例")
humans['speed'] ='fast'
print(humans)
print("删除键值对")
#使用del语句
del humans['speed']
print(humans)
print("\n")

#定义由类似对象组成的字典
favorite_language ={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
print("sarsah's favorite language is"+favorite_language['jen'].upper()+".")

#如何去便利整个字典
"""利用for循环来遍历    
for  key，value in dictionary_name.item():
     print("\nkey :"+key)
     print("value :"+value)
"""
print("item()这个方法是用于传送键值对")
for key,value in favorite_language.items(): #python当中提供一种方法用于返回key-value的键值对
    print("\nkey :" + key)#这里的key只是一个名称 为了显示键值对的左侧
    print("value :" + value)#这里的value只是一个名称 为了显示键值对的右侧
for name , language in favorite_language.items():
    print("\nname:"+name)
    print("language:"+language)

print("\n如果只想返回键值对中的key，那么keys()提供了一个不错的选择")
for key in favorite_language.keys():
    print("\nkey"+":"+key)
print("打印只包含value的值,利用values()")
for value in favorite_language.values():
    print("\nvalue :" + value)

#按照顺序遍历字典  这个排序只是利用a~z的字母顺序排序
print("\nsorted()函数用于去排列字典中的顺序")
for name in sorted(favorite_language.keys()): #for循环跟着的in的后面都是一个列表/元组/字典型的东西
    print(name.upper()+",thank you for taking the poll")
print("\n按照值方式顺序打印")
for language in sorted(favorite_language.values()):
    print("language:"+language.title())

#嵌套
print("\n打印字典的嵌套，在列表中存放字典")
alien_0 ={'color':'green','points':5}
alien_1 ={'color':'yellow','points':10}
alien_2 ={'color':'red','points':15}

aliens =[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#字典列表 ：就是字典存放在列表当中
""" 
    设计一个空的列表，用于循环存放数据字典，并且从列表中用一直方式打印列表中的值。
    range():这个方式实际上就是 设置一个值 用于规定循环的次数
"""
print("\n使用range()函数，来生成多个字典")
fruits =[]

for fruit in range(30):
    new_fruit = {
        'color':'red',
        'suger':'s+',
        'speed':'slow'}
    fruits.append(new_fruit)#append方法只能添加到列表里面去,  字典是可以加到列表里面的
for fruit in fruits[:5]:
    print(fruit)
print("...")

print("Total number of diction :"+str(len(fruits)))

#列表字典：就是在字典中存放列表 在value的位置上
human_beings ={  #定义一个字典包含两个列表
    'sex':['男','女'],
    'color':['black_man','white_man','yellow_man']
}
for sexs in human_beings['sex']:#调用键值对
    print("\nkey:"+sexs)
    for colors in human_beings['color']:
        print("color:"+str(colors))
print("\n")
""" for colors in value:
        print("color:"+colors)
print("over")"""

pizza ={
    'crust':'thick',
    'topping':['mushrooms','extra']
}

print("you ordered a " +pizza['crust']+"_crust pizza"+"with the following toppings")

for topping in pizza['topping']:
    print("\t" +topping)