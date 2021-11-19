"""" 第二章 多行注释 """
"""
注意事项：
1、python当中的代码不要太长+
2、每行的代码都是一条语句，并且以回车的方式结束
3、代码后面加一个  \ python解析器就会把它当做一个语句 只是认为他是换行
4、python当中的整数都是int型，并且对整数的范围没有限制

进制数
二进制：0b开头
八进制：0o开头
十六进制：0x开头

字符串
1、单引号当中不允许有单引号，同理适用于双引号 （用一类型的引号之间不允许同样的引号）
2、三重引号可以作为换行
"""
abc = ''' 锄禾日当午，
汗滴禾下土，
谁知盘中餐，
粒粒皆辛苦'''
print(abc)
#单行注释
''' 这是文档字符串 '''
print(2**3)
'''python中的特殊地方 ，不是很精确'''
print(0.2+0.1)

#在python中str方法
""" str() 转字符串"""
age = 23
print("happy,"+str(age)+"rd birthday")
values = int(age)
print(values)
#python中的tittle会把字符串的每一个的首字母大写
""" python当中对大小写没有特别的识别"""
message = "simple is better than complex: "
print(message.title())
print("\n")

""" python是区分大小写的"""
car = 'bmw'
if car == 'BMW':
    print("TRUE")
else:
    print("over")

"""试着打印1~20"""
for number in range(20):#range函数是从0开始，并且这是整数类型扫描
    print(number+1)