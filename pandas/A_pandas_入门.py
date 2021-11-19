'''
https://datawhalechina.github.io/joyful-pandas/build/html/%E7%9B%AE%E5%BD%95/index.html

'''

'''列表推导式'''
def my_func(value):
    return value**2

'''第一种列表推导式(for循环）'''
print([my_func(i) for  i in range(5)])

'''双重列表推导式（嵌套for循环）'''
print([m+'_'+n for m in ['a','b'] for n in ['c','d']])

'''判断语句'''
print('cat' if 2>1 else 'dog')

'''结合判断和for循环'''
L = [1,2,3,4,5,6,7]
print([i if i<=5 else 5 for i in L])







'''匿名函数和map函数'''

my_funcs = lambda x: 2*x#这里相当于给一个函数起名字 名字叫lambda 参数是x 输出是x*2
my_funcs_2 =lambda x,y:x*y
# my_funcs_2(3,4)

'''实际操作  单个参数'''
print([(lambda x:2*x)(i) for i in range(5)])
#这里相当于把i作为参数传给这个lambda函数 （i）

print(map(lambda x :2*x,range(5)),end="\ncomparable")#这里只能打印地址 因为是map

print(list(map(lambda x :2*x,range(5))))


'''两个参数时候  list()方法可以转化为列表'''
list_map = list(map(lambda x ,y:y*x,range(5),range(5)))
print(list_map)


'''测试打包效果'''
print('\n')
new_list=list('abc')#list是把里面的字符串拆成一个个的存到列表里面去，
# print(new_list)

l1,l2,l3 =list('abc'),list('def'),list('gbk')
value =list(zip(l1,l2,l3))#zip是按数据结构打包
new=[]
print(value)#看一下打包效果
new.extend(l1)#拆成一个个
print(new)

for i,j,k in zip(l1,l2,l3):
    print(i,j,k)



'''放大招-------------字典映射'''
m=dict(zip(l1,l2))
print(m)#里面的元素一一对应



import numpy as np
'''需要的numpy基础'''
np.random.randn(3)#生成N（0，1）的标准正态分布 ，如果维度给的多则是矩阵形式
np.random.rand(3)#生成等差数列 在0-1之间 ，如果维度给的多则是矩阵形式

sigma ,means = 2.5,3
means+np.random.randn(3)*sigma
np.random.randint(low=5,high=15,size=(5,5))#可以设定一个范围大小的值 最大是15最小是5

print(np.random.random(8))#随机生成一个列表 列表元素在0-1之间 8个




####################################






