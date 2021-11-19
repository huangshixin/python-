""" 8章 函数 """

import sys
sys.setrecursionlimit(100000) #设置最大跌打数recursionlimit
"""
1、定义一个函数的语法
2、传递参数给函数：无参函数与有参函数
3、关键字实参 ：将某些形参赋值
4、返回值
5、返回字典
6、递归
7、传递列表
matrix /mei/  retriever /ri tri ve/
"""

#定义一个函数的语法
"""
定义部分 def function_name():
           xxxxxxxxxxx
调用部分  function_name();
"""
#定义函数
def get_user():
    print("there is possible using guns to looot American")
#调用函数 configuration ：结构
get_user()

#传递参数给函数
"""user_name = input("Please enter a string into the system :")
def get_hospitile(user):#这里的user就是形参
    print("hello,"+user)
get_hospitile(user_name+"\n") #这里的方法后面就是实参，不过实际参数通过控制台输入
"""
#关键字实参
"""
目的是为了引进一种方法，讲想要传递的值传递到对应的位置里面去
"""
animal = 'hamster'
pet = 'harry'
def get_pet_name(animal_name,pet_name):
    print("MY PET's type is :"+animal_name)
    print("my pet's name is :"+pet_name)
get_pet_name(animal,pet)
print("以下显示关键字实参调用")
get_pet_name(animal_name='HUSKY',pet_name='哈K')
print("验证参数倒放，但是传参固定的情况下是否可以成功")
get_pet_name(pet_name='哈K',animal_name='HUSKY'+"\n")

#默认值调用
"""在形参的位置直接赋予实参"""
def describe_pet(animal_names,pet_name = 'KK'):
    print("THE TYPE OF MY DOG IS:"+animal_names)
    print("my "+pet_name.title()+" is a hostile dog.")
#此时我不再赋予函数pet_name新的值
"""当不赋予值的时候系统会默认他原来的值"""
describe_pet('husky')
#此时打印赋予新值得时候的效果
describe_pet('husky',pet_name='qiuqiu')
#此时打印全部
describe_pet('husky','k_s')
print("\n")

#返回值
"""语法：
  Python当中对于函数以及形参是不赋予初始的类型的，所以当要考虑到系统当中的数值类型时，Python在实参方面做了把控
  若要返回function当中的值， 采用return语法
"""
def COMPARE_SIZE(values_1,values_2):
    if int(values_1) >= int(values_2):
        return int(values_1)
    else:
        return  int(values_2)
print("打印最大值")
print("MAXINUM IS:"+str(COMPARE_SIZE(315,124)))  #我一开始函数比较的是整数类型，但是我打印的值是str类型啊

#给函数设定一个可选择的值
"""什么意思呢？
就是假设我不知道，这个参数是否要传入，但是我又希望当我不传入这个值得时候这个函数依旧可以运行
"""
def get_full_name(first_name = "",last_name = " ",middle_name = ""):
    #对其中不确定的形参设定一个空的实参
    print("LINKED AMONG STRINGS")
    if middle_name:#这个代表middle_name是存在的
        full_name = first_name + "." +  last_name+ "." + middle_name
    else:
        full_name = first_name + "." + last_name
    return full_name.title()
#调用
print("PRINT the first STRING："+get_full_name('THOMS','L','HSX')+"\nPRINT THE SECOND STRING："+
get_full_name('THOMS','HSX'))

#返回字典
"""回顾如何添加键值对到字典里面典_name['']"""
persons = {}
def build_person(first,last):
    first_name = str(first)+"s"
    last_name = str(last)+"s"
    persons[first_name] = first  #列表当中才采用append的方法
    """#[]里面本身就是字符串所以不需要加'',不然应用的值就会被覆盖 ，"""
    persons[last_name] = last
    return persons
print("打印字典persons")
build_person('xiaoming','xiaohua')
build_person('zhanghongyi','liyanchen')#字典被更新了
print(persons)

#汉漠塔的递归
"""def compute_number(values):
    if values ==1:
        return 1
    elif int(values) ==0:
        return 1
    else:
        return  compute_number(values)+compute_number(values-1)
message = input("please enter a number less than 20:")

def fabonacci(n):
    if n <=2:
        v = 1
        return  v
    v = fabonacci(n-1) +fabonacci(n-2)
    return  v
print(fabonacci(12))
print("\n")
"""

"""递归"""
def recursion(vk):
    if vk <= 1:
        v =1
        return v
    else:
        return recursion(vk-1) + recursion(vk)

print(recursion(100))

#传递列表
"""传递一个列表给函数，函数拿到该列表后对列表的信息进行处理"""
"""def greet_user(user_name):
    for user in user_name:
        msg = "HEELO,"+user.title()+"!"
        print(msg)
usernames = ['hsx','cxj','djm']
greet_user(usernames)

#prohibit rectify table:
def mes_user(value):
    for user in value:
        if user:
            print("hello,"+value)
            value.remove(user)
user_friends = ['hsx','cxj','djm','xjj']

mesg = user_friends[:]

"""

#传递任意数量的实参
#   *toopings 这是一种形参： 语法：  *name 会把各种实参包含在内
def make_pizza(*toopings):
    print(toopings)
print("任意数量的实参")
make_pizza('sdsdsdsdas')
make_pizza('dsads','sdsa','dsadsad')

#导入模板
"""
导入某个模块
import model_name

导入某个函数
from model_name import function_name_1,function_name_2

设计一个新的名字
import model_name as new_name

调用某个函数
function_name()

导入所有函数
from model_name import *
"""

#如果希望导入的模块不会报错需要这么做
"""
 把你的文件夹设置为source root
 方法： 右键---make directory as ---source root
"""




