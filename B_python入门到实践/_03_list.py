#what is list for python?
""" motorcycles = ['trek','bicycle','motor','vehicle']"""

""" 修改 rectify 需要通过用一种角标的方式执行"""
motorcycles = ['trek','bicycle','motor','vehicle']
print(" 初始值表示")
print(motorcycles)
print("修改角标为0处的数值")
motorcycles[0] = 'motorbike'
print(motorcycles)
print("\n")

"""通过角标的方式去索引你所想要输出的值"""
print("通过角标的方式去索引你所想要输出的值")
print(motorcycles[3])
print("字符串的拼接")
print("My favorite motorcycle is"+motorcycles[2]+"\n")

"""在列表中添加一些值"""
print("在列表的，末尾插入我们需要的新值")
humanbeings=['black people','white people']
print("打印初始的列表值")
print(humanbeings)
#append的作用是在末尾添加数据,需要具体的值
print("打印添加后的列表值")
humanbeings.append('yellow people')
print(humanbeings)
print("用insert的方法插入新的值")
humanbeings.insert(0,'alien')
print("打印插入后的效果值")
print(humanbeings)
humanbeings.insert(4,'anybody')
print(humanbeings)
#用角标为-1的方式去打印最后一个值
print(humanbeings[-1])

"""删除列表中的一些值"""
print("利用pop去弹出列表中的值，每次都从列表的最后把值弹出")
fruit =['apple','banana','orange','pea','peach','watermelon','melon','lemon']
print("打印原始值")
print(fruit)
print("弹出最后一个并打印列表")
#pop能弹出任意位置的值（角标内），当使用pop的时候需要考虑这个值以后还会用到那么就是用pop，再也不用了 ，那就使用del
fruit.pop(0)
print(fruit)
#采用del方式进行操作，del的方式是去通过角标识别的方式删除列表中的值
del fruit[0]
print(fruit)
#根据实际的值去删除列表中的值    remove
fruit.remove('watermelon')
print(fruit)
print("\n")

#对列表进行拍寻
schools =['middleSchool','university','college','high-School','juniorSchool']
print("打印初始值并且排序")
print(schools)
#sort是长期排序  sorted是短期怕排序
print("打印sorted展示的效果")
print(sorted(schools))
print("打印sort展示的效果(永久排序)"+"\n")
schools.sort()
print(schools)
print("打印sort反向排序的效果")
schools.sort(reverse=True) #反向排序
print(schools)
print("\n")
#计算列表中的元素个数
cars = ['bmw','toyota','audi','subaru']
print(str(len(cars)))  #计算出的值打印成字符串




#####################################
"""
以下这些方法都是改变数据 但是不返回东西


sort默认  从小到大排序  改变原来的数据结构  reverse=True则反向排序  
sorted 默认 从小到大排序  不改变原来的数据结构  reverse=True
reverse()  自带的方法 从后往前排序
"""