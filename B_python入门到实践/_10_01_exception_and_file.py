# 异常处理
""" python当中使用 try---except处理异常"""
"""
summarize：
try 中存放可能会报错的代码
except 里面存放报错的反馈
else 里面放 try执行成功后需要执行的语句
"""
#zeroDivisionError
""" 以下示范try --except的使用方式"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't division by zero\n")

"""使用异常语句。避免系统崩溃"""
print("Give me two numbers 'A' and 'B',AND I will division  them")
print("please enter 'q' to quit")

while True:#python中 true的关键字是需要首字母大写的   Reverse =True
    first_number = input("enter the first number:")
    if first_number == 'q':
        break
    second_number = input("\n enter the second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
        print(answer)
        break
    except:
        print("\nwe find an error in this location\n")

"""
系统发现try-except无法满足现况了，于是引入try-except--else

else里面存放的是try成功执行时候才执行的语句放在 else
"""

while True:
    the_first_case = input("enter the first case into the control panel:")#panel[怕no]
    if the_first_case == 'q':
        break
    the_second_case = input("enter the second case into the control panel:")
    try:
        #try执行失败后 ，直接不执行try后面的语句，而到了except
        result = int(the_first_case)/int(the_second_case)
    except:
        print("THE RESULT FIND AN UNEXPECT ERROR")
    else:
        print(result)
        print("you can input 'q' to end this program")#programing 程序设计 v 动词

def compute(value_1=5,value2=2):
    try:
        answers = value_1/value2
    except ZeroDivisionError:
        print("ZeroDivisionError")
    else:
        print(answers)#else可以打印到anser的值，其实很简单，try是执行成功时候else才执行的
        print("the programing will quit  now")
compute()#不赋值就是默认初始值
compute(3,2)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

#执行filenotfoundexception
file_name = 'alien.txt'
"""no是形容词  not是副词"""
try:
    with open(file_name) as file_names:
        file_names.read()
except FileNotFoundError:
     print("No files found on this computer")

