# if 语句
cars = ['audi','bmw','subaru','toyota','Mercedes Benz']
"""if语句的语法是 if xxx==:   else xx==: """
for car in cars:
    if car == 'bmw':     #python当中比较运算符写是  不区分的    估计有特别的函数
        print("如果值等于bmw")
        print(car.upper())
    else:
        print("车的名字是：")
        print(car.title())

#python是不区分大小写的

print("判断是否相等：需要用到python当中的一些判定符 ！= == >= =<")
request_stooping = 'mushroom'
plant =['request_stooping']
if request_stooping == 'mushrooms':
    print("request_stooping is:mushroom")
else:
    print("That is not plant :"+str(plant[0]))

#python当中有逻辑运算符 and or
age_0 = 18
age_1 =19
print(age_0 == age_1)
print(age_0 == age_1 or age_0 <=age_1)
print(age_0==age_1 and age_0 !=18)

#检查特定值是否在列表中  语法 利用 in 和 not in
print("\n")
request_stoop = ['mushroom','onions','pineapple']
if 'mushroom' in request_stoop: #双重if循环
    print(True)
if 'watermelon' not in request_stoop:
    print("maybe watermelon is not fruit")
else:
    print("test over") #布尔表达式就是true 和false

#if 循环当中有种if-elif-else 这种形式
Lihua = 'female'
if Lihua == 'male':
    print("\n这个人是个男性\n")
elif Lihua !='femle':  #负责如果 写成elif
    print("\n这个人可能是女的\n")
else:
    print("\n这是个妹子\n")

#使用if语句进行处理列表
requested_stoop = ['mushroom','green peopers','extra chese']

for request in requested_stoop:
    if request == 'mushroom':
        print("蘑菇")
    elif request =='extra chese':
        print("我也不知道什么东西")
    else:
        print("绿色植物")
print("循环结束")

#判断列表是否为空
green = []

if green: #这种方法就是定义列表为空
    for greens in green:
        print("Adding"+greens+".")
    print("\n 列表为空")
else:
    print("Are you sure you want to a plain pizza?")


