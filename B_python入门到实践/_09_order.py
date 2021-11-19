# 第九章  类
""" menu"""
#创建和使用类 class order_name():
#给属性设置一个默认值
#修改属性的值
#通过方法去修改属性的值
#继承
#创建实例
#将实例设置为属性

class DOG():#类的首字母要大写
    """模仿小狗"""
    def __init__(self,name,age):
        """
        __init__后面必须有这个self，这个在类被
        这是Python当中的一种特殊的方法。他会在类被引用的时候自动调用
        """
        """初始化"""
        self.name = name#以self为前缀的变量可以允许类当中所有的方法使用
        self.age = age#要使用 那么那些方法也需要包含self

    def sit(self):
        """sit"""
        print(self.name.title()+"is now sitting.")
    def roll_over(self):

        print(self.name.title()+"is now roll over")

#调用系统中的_init_
my_dog = DOG('husky',6)

print("My dog is "+my_dog.name.upper())
print("My dog is "+str(my_dog.age))

#给属性设置一个默认值
""" 传递值的时候要注意你的值是什么类型 需要在调用的时候做好相应的转换"""
class Car_1():
    """初始值"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 #直接给这个新的变脸设置一个默认值
    def get_descriptive_name(self):
        long_name = str(self.make)+" "+self.model+" "+self.year
        return long_name.title()
    def get_odometer(self):
        "print一条信息"
        print("This car has"+" "+str(self.odometer)+" miles on it:")
    def rectify_value(self,odometer):
        #通过方法去修改属性的值
        self.odometer = odometer
    def Add_miles(self,odometer):
        #通过方法来累积公里数
        self.odometer += odometer

small_CAR = Car_1(4,'BMW','toyota')
print(small_CAR.get_descriptive_name())
small_CAR.get_odometer()
print("check this result by the following code below")
small_CAR.rectify_value(15)
small_CAR.get_odometer()
small_CAR.Add_miles(2)
small_CAR.Add_miles(6)
small_CAR.get_odometer()

#修改属性的值
# 在调用的时候改变函数的值 small_CAR.odometer = 23

#课后习题
class User():
    def __init__(self,first_name,last_name,sex,favour):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.favour = favour
        self.attribute = 0
    def describe_user(self):
        long_name = self.first_name +"."+ self.last_name +"is a"+" "+self.sex+","+" She has a favour about: c"+self.favour
        return  long_name
    def greet_user(self):
        """打印称谓语"""
        print("Hello,"+self.first_name+" . "+self.last_name+".")
    def set_attribute(self,attribute):
        #新增属性的方法
        self.attribute = attribute
    def increment_login_attempts(self):
        self.attribute += 1
        return self.attribute

    def reset_attribute(self):
        self.attribute = 0

test_user1 = User('djm','xjm','女','swimming')
test_user2 = User('hsx','hxx','male','football')
test_user3 = User('chj','chl','female','running')
print(test_user1.increment_login_attempts())
print(test_user2.increment_login_attempts())
print(test_user3.increment_login_attempts())
print("This number is :"+ str(test_user3.set_attribute(test_user3.attribute)))
test_user3.reset_attribute()
print("Reset successful or not")
print(test_user3.attribute)

#继承
"""
 继承的分类为两个类：父类和子类
    一个类继承另一个类的时候会自动的继承上一个类的属性和方法（attribute and method）
    语法：
    clas Car():
    class ElectricCar(Car): 把父类放在子类的圆括号里面
"""
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.read_odometer_name = 70#定义一个新的值，在超类中
    def get_describe_name(self):
        long_namw = str(self.year)+" "+self.model+" "+self.make
        print(long_namw.title())
    def read_odometer_name(self):
        """打印这个超类值"""
        long = "This car has been driven "+str(self.read_odometer_name)+" miles on it"
        return  long
#子类
class ElectricCar(Car):
    """
    在子类中如果需要父类的方法则直接使用继承
    """
    def __init__(self,make,model,year):
        """父类提供了一个super()方法，用于调用父类的init方法"""
        super().__init__(make,model,year)

#调用
my_tesla = ElectricCar(model='tesla',year=2,make='red')

#因为python中print函数需要返回值，如果你在print函数中所放的函数没有返回值，那么print将会return None
"""
这件事要求我们：
如果你的方法里面有return语句，那么结尾调用的时候可以用print 这样就不会出现none
与此同时：如果方法是print语句，那么直接调用my_car.method_namw()
"""
my_tesla.get_describe_name()

print("\n")

"""
创建一个电池类：目的就是在一个类的方法中去创建某个类的实例 把他作为一种属性

"""
class Bettry():

    def __init__(self,battery_size=70):
        """设置初始值"""
        self.battery_size = battery_size

#给子类定义属性和复写父类的方法
class metroCar(Car):
    def __init__(self, make, year, model):
        """这个方法是不能复写的"""
        super().__init__(make, model, year)
        self.type = Bettry(60)

    def get_describe_name(self):
        """复写父类的方法：需要同样的名字和方法类型包括了形参"""
        print("This a new method")
    def get_bettry_state(self):
        """不设置初始值，那么电池默认为70"""
        print("This battery's capacity is "+ str(self.type)+"-kw battery")

car_test = Car('aaa',year=2,model='model')
car_test.get_describe_name()

my_metroCar = metroCar('aaa',year=2,model='model')#定向赋值语句要放在最后，或者从某一处开始后续都要精确赋值
my_metroCar.get_describe_name()
my_metroCar.get_bettry_state()
#将实例作为属性




