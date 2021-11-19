#        第十一章   测试代码
"""
我们编写代码的时候可以为其编写测试代码
"""
def get_formatted_name(first,last):
    """ generate a nearly formatted full name
    format:
    n.	总体安排; 计划; 设计; (出版物的) 版式，开本; 格式;
    v.	格式化; 安排…的版式
    """
    fullnames = first + last
    fullname = str(first)+" "+str(last)
    return  fullname.title()+str(fullnames)
#python在字符串拼接的时候用的是单引号  在print语句中使用的是双引号

def get_full_name(prior,next):

    fullname = prior+''+next
    return "\tfull name is "+fullname.tittle()


def get_formatted_names(prior,next,middle=''):
    """设定某个人的全名"""
    if middle:
        full_name = prior+' '+middle+' '+next
    else:
        full_name = prior+''+next
    return full_name.upper()