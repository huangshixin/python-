#分析文本
print("利用split方法去分割字符串，按照空格分割") #死 per lei t
filename = r'C:\Users\15159\Desktop\alice in wonderland.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
        print(contents)
except FileNotFoundError:
    msg = "Sorry,the file " + filename +"does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("THE FILE "+filename+"has about "+str(num_words)+"words.")

#防止程序失败的时候一声不吭
"""python当中提供了一种 pass语句"""
def count_words(filenames):
    try:
        """存放你要执行的语句"""
    except:
        pass #不做任何反应
    else:
        abc = filenames.split()#分裂一下
        num_word = len(abc)
        print("")
filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for file in filenames:#利用函数去计算多少个单词
    count_words(file)


#讲解JSON串
"""json （JavaScript object notation）
用于存放用户的数据，把数据存放到文件里面去
json.dump()  json.load()
"""
#导入json串
import  json
#设计一个列表
numbers = [2,3,4,5,7,11,13]

name = 'numbers.json'
with open(name,'w') as names:
    #利用json.dump函数把数字列表numbers的值存放到name里面去
    """
    1、定义json
    2、设计列表
    3、设置一个json结尾的文件名
    4、开始写操作，并且给文件夹命名为names
    4、把列表写到文件中，利用dump
    """
    json.dump(numbers,names)


#读取json
"""利用load读取json到内存"""
with open(name) as f_obj:
     nbrs = json.load(f_obj)#python当中的值需要先赋予到某个变量在吧这个值打印出来
print(nbrs)