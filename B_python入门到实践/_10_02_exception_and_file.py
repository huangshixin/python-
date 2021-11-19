# 第十章 python当中的异常处理

"""
从文件中读取数据
with open('address') as folder_name:      单引号
1、首先利用open()函数去识别文件的位置
2、用read()方法去读取
3、with关键字
"""
with open('C:\\Users\\15159\\Desktop\\hsx.txt') as file_name:
    """
    地址问题：可能遇到转义字符的问题
    1、把地址改变为"\\"的格式
    2、把地址改变为"/"的格式
    3、在地址前加"r" 系统则会把这个当成原始地址  r'address'
    """
    contents = file_name.read()
    print(contents)

#逐行读取文件
"""利用for循环来逐行读取文件"""
#展现一个创新
print("事先给file变量定义一个文件的地址，然后采取for循环的方式按行读取文件内容")
file = r'C:\Users\15159\Desktop\test.txt'
with open(file) as file_2:
    for line in file_2:
     print(line)
print("是否好奇如何消除空白行，python提供了rstrip（)方法")
print("line.rstrip（)方法")
with open(file) as file_3:
    for lines in file_3:
        print(lines.rstrip())
print("\n")

#with关键字
"""with关键字内的的变量只能在自己内部使用，如果要在with代码块外部使用则需要，利用readlines()"""
print("在with代码块外部使用则需要，利用readlines()")
with  open(file) as file_object:
    name = file_object.readlines()
for file_4 in name:
    print(file_4.rstrip())
print("\n")

#使用文件的内容
"""实际就是读文件，拿文件中的数据去拼接"""
#测试数据
file_path = r'C:\Users\15159\Desktop\test.txt'
with open(file_path) as file_final_test:
    for test_name in file_final_test:
        if '164645' in test_name:
            print("TRUE")
            break
        else:
            print("FALSE")
print("python在读取文件的时候，往往是把文件读取为字符串的格式，如果需要读取数字型文字，你需要用int()/float()读取为浮点型")
print("\n")

#分析一百万位的大型文件
"""question
1、把文件中每一行的数据拼接成一个字符串
2、读取字符串，并且打印前xxx位的字符串
"""
string_file = ""
with open('C:\\Users\\15159\\Desktop\\hsx.txt') as file_name:
    for file in file_name:
        string_file += file
print("第一次打印看效果"+string_file)
print("二次打印"+string_file[:26]+"...")

#写入文件
print("\n")
"""解释一下工作原理
python提供了四种对文件处理的模式(model)  module：单元、模块
'a':add 添加内容但是不覆盖
'w':write 直接覆盖之前的内容
'r':read
'r+':read+w
"""
#explain
"""
如果没有固定模式：则系统默认只读
如果没有文件，系统则会创建文件
w模式，如果模式存在，你写的时候会覆盖
a 就是add操作
"""
filename = 'C:/Users/15159/Desktop/programing.txt'
with open(filename,'w') as filenames:
    #覆盖操作
    filenames.write("I LOVE PROGRAMING using python\n!")
    filenames.write("I LOVE PROGRAMING using python!"+"xxxxxxxxxxxxx")
with open(filename,'a') as filenames:
    #附加操作，额外加内容进去但是不覆盖
    filenames.write("I LOVE PROGRAMING using java\n!")
    filenames.write("I LOVE PROGRAMING using python!" + "l adore you\n")
with open(filename,'r+') as filenames:
    file = filenames.read()
    print(file)
    filenames.write("cccc")
    files = filenames.read()
    print(files)
