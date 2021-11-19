#继承
#explain
"""
1、继承父类需要复写init方法，但不一定要复写其他的方法
2、复写父类的方法需要方法名和参数类型一致
3、

"""
class Car():
    """一次模拟汽车的简单测试"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return  long_name
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading) + "miles on it")
    def update_odomter(self,mileage):#这里的mileage的数值可以在计算的额时候传入
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print(str(self.odometer_reading))
        else:
            print("You can't roll back an odometer!")

#将实例作为一种属性
class Battery():

    def __init__(self,battery_sizes =70):
        """若生成电池对象时候，没有设置新的电池大小值，系统会选座位默认值"""
        self.battery_size = battery_sizes
    def describe_battery(self):

        print( "This car has a "+str(self.battery_size)+"-kw battery")

#定义一个子类
class ElectricCar(Car):

    def __init__(self,make,model,year):
        """ 子类中的super指针用于调用父类中的init方法"""
        super().__init__(make,model,year)
        """给子类定义属性和方法 """
        self.battery_size = 70
        self.type = Battery()
        """定义一个子类的方法"""
    def describe_battery(self):
        print("This capacity of battery is"+str(self.battery_size))
    def read_odometer(self):
        print("这个方法是用于测试复写父类的方法的效果")
my_tesla = ElectricCar('tesla','model_s',2020)
print(my_tesla.get_descriptive_name())
my_tesla.get_descriptive_name()#调用子类自己的方法


#调用
my_car = ElectricCar('bmw','x7',2020)
my_car.type.describe_battery()
