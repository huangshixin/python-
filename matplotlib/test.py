from matplotlib import pyplot as plt
from scipy.spatial import distance
import numpy as np

"""
我想计算损失函数 ，并且把这个值打印出来
"""
def create_list(value):
    '''随机生成一个10类  20个的数据模拟的训练数据'''
    # np.random.seed(272)
    x=[x for x in np.around(np.random.random(value)*10,0)]
    return np.random.permutation(x)


#真实值
def create_real_value():
    c= [2.0, 8.0, 9.0, 3.0, 2.0, 2.0, 2.0, 3.0, 6.0, 2.0, 6.0, 5.0, 7.0, 5.0, 1.0, 5.0, 9.0, 3.0, 9.0, 7.0]
    return c

# def main():
#     epoch =10
#     value = 20
#     newList = []
#     for i in range(epoch):
#         '''存入列表'''
#         compute_value = np.around(distance.euclidean(create_list(value),create_real_value()),0)
#         newList.append(compute_value)
#     print(np.arange(10))
#     print(newList)
#     plt.xlabel(xlabel='epoch')
#     plt.ylabel(ylabel='loss function')
      #散点图
#     plt.scatter(x=[i+1 for i in np.arange(10)],y=newList,c='red', edgecolors='none',s=40)
#     plt.show()


def main():
    epoch =10
    value = 20
    newList = []
    for i in range(epoch):
        '''存入列表'''
        compute_value = np.around(distance.euclidean(create_list(value),create_real_value()),0)
        newList.append(compute_value)
    print(np.arange(10))
    print(newList)
    plt.xlabel(xlabel='epoch')
    plt.ylabel(ylabel='loss function')
    plt.title('lossfuncrion')
    x = [i + 1 for i in np.arange(10)]
    y=newList
    plt.plot(x,y,c='red')#plot不能在内部设置
    plt.show()
main()


