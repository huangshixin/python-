import json
#json需要导入json，unittest需要导入unittest
#refactor 重构
""" 将代码划分为一系列完成具体工作的函数，所以对函数进行重构 """
def greet_user():
    """问候用户"""
    new_people = r'C:\Users\15159\Desktop\username_j.json'
    try:
        with open(new_people) as gr_obj:

            greet_name = json.load(gr_obj)
            print(greet_name)
    except FileNotFoundError:
        username = input("输入一个名字")
        with open(new_people,'w') as gr_obj:
            json.dump(username,gr_obj)
            print("这个文件已经被写入系统里面")
    else:
        print("Welcome back,"+new_people +"!")

greet_user()

print("加注释的时候一定要小心，不能存在\这种形式，因为会出现错误，只能修改文件储存路径")

username = input("please enter a name into the control panel")

filenames ='C:\\Users\\15159\\Desktop\\remember_me.json'
while True:
    try:
        with open(filenames,'w') as re_obj:
            json.dump(username,re_obj)
            print( " We'll remember you when you come back,"+username+"!")
            break
    except :
        print("The word '"+username+"'"+"mismatch this program's expectation") #expection是个动词 expectation名词

try:
    with open(filenames) as f_obj:
        username = json.load(f_obj)#load 单词意思是加载
except FileNotFoundError:
    user = input("what's your name?")
    with open(filenames,'w') as f_obj:
        json.dump(user,f_obj)
        print( " We'll remember you when you come back,"+user+"!")
else:
    print("Welcome back,"+username +"!")  



