import torch
import numpy as np
import random
'''
生成数据集模块，以及按照btach打印
************************************************************************************************************************
线性回归输出的是一个连续值

由于线性回归和softmax回归都是单层神经网络，
它们涉及的概念和技术同样适用于大多数的深度学习模型。
我们首先以线性回归为例，介绍大多数深度学习模型的基本要素和表示方法
************************************************************************************************************************
假定我们希望在一个线性模型上训练一组参数（weight）来拟合我们的样本的特征

首先我们需要确定有哪些参数、以及线性模型（---）

其次,我们训练出参数后，我们要构建单个的损失函数 loss

最后我们计算全部样本的loss，并最小化它，最小化的方式一般是梯度下降来优化（并用到求导）

解析解：最小化问题可以直接用公式表达
数值解：只能通过优化算法的有限次迭代模型参数来尽可能降低损失函数的值

mini-batch stochastic gradient descent（小批量随机stochastic梯度下降方法）

在每次迭代中，先随机均匀采样一个由固定数目训练数据样本所组成的小批量（mini-batch）B\mathcal{B}B，
然后求小批量中数据样本的平均损失有关模型参数的导数（梯度），最后用此结果与预先设定的一个正数的乘积作为模型参数在本次迭代的减小量
'''
#定义两个1000维的向量
import torch
from time import time

a = torch.ones(1000)#np.ones
b = torch.ones(1000)

#向量相加的一种方法是，将这两个向量按元素逐一做标量加法
start = time()#获得当前运行时间
c = torch.zeros(1000)
for i in range(1000):
    c[i] = a[i] + b[i].T#向量对应位置相加
print(time() - start)
# print(c)

#矢量加法(相当于向量的对应位置做运算）
'''比前一种省时间'''
start = time()
d = a + b
print(time() - start)
print(d)

a = torch.ones(3)
b = 10
print(a + b)

'''
tensor([11., 11., 11.])
'''






#随机生成一个1000数据 两列的矩阵'''
num_inputs =2
num_examples =1000
true_w =[2,-3.4]
true_b =4.2
feature =torch.randn(num_examples,num_inputs,dtype=torch.float32)#随机生成1000行两列的（1000个2列）
# print(type(feature))#<class 'torch.Tensor'>
# print(np.shape(feature))#torch.Size([1000, 2])
label =true_w[0]*feature[:,0]+true_w[1]*feature[:,-1]+true_b
label +=torch.tensor(np.random.normal(0,0.01,size=label.size()),dtype=torch.float32)


def data_iter(batch_size,feature,labels):
    '''获取数据集中样本的个数'''
    num_example = len(feature)#可以确定的是feature是列表中存放的列表的形式

    #生成一个0-len（feature）-1的列表'''
    indices =list(range(num_example))

    #给列表进行一次洗牌'''
    random.shuffle(indices)

    for i in range(0,num_example,batch_size):
        #迭代次数从0开始，到len（feature）-1结束,  其中跨度是batch_size'''

        j =torch.LongTensor(indices[i:min(i+batch_size,num_example)])
        '''
        【0：10】、 【1：11】、。。。。。。。。。。。。【len(feature)-10，len(feature)】
        通过索引获得他的元素值 index_select(0,j)
        到这里你可能就明白yield和return的关系和区别了，带yield的函数是一个生成器，而不是一个函数了，这个生成器有一个函数就是next函数，next就相当于“下一步”生成哪个数，
        这一次的next开始的地方是接着上一次的next停止的地方执行的，所以调用next的时候，生成器并不会从foo函数的开始执行，只是接着上一步停止的地方开始，然后遇到yield后，return出要生成的数，此步就结束
        '''
        yield feature.index_select(0,j), labels.index_select(0,j)# take函数根据索引返回对应元素


# #读取第一个小批量数据样本（从0 每次10作为跨度）
batch_size =10
for x ,y in data_iter(batch_size,feature,label):
     #返回两个值 还可以用循环接
     print(x,y)
     break

'''
************************************************************************************************************************
'''





'''
创建一种模型
'''
from torch import nn#各种神经网络都在里面
class LinearNet(nn.Module):
    '''
    Module既可以表示神经元 也可以表示多种神经网络
    '''
    def __init__(self,n_feature):
        super(LinearNet, self).__init__()
        self.linear = nn.Linear(n_feature,1)#相当于定义了一个全连接层


    #forward前置网络的定义
    def forward(self,x):
        y = self.linear(x)
        return y

net =LinearNet(num_inputs)
print(net)

# #以上线性函数还有其他的写法
# net =nn.Sequential(nn.Linear(num_inputs,1))
#
# #写法二
# nets=nn.Sequential() xikunxiu
# net.add_module('linear',nn.Linear(num_inputs,1))
#


'''
****************************************************************************************************
#获取所有的训练参数
****************************************************************************************************
'''
for param in net.parameters():
    print(param)





'''初始化模型参数'''
from torch.nn import init

#这个只有在定义为modual和Sequential时候才可以 否则 net.linear.weight
'''
# init.normal_(net[0].weight,mean=0,std=0.01)
# init.constant_(net[0].bias,val=0)#也可以直接修改bisa的data：net【0】
'''
init.normal_(net.linear.weight,mean=0,std=0.01)
init.constant_(net.linear.bias,val=0)




#定义损失
loss=nn.MSELoss()#均方差损失





#定义优化器
import torch.optim as optim

optimizer =optim.SGD(net.parameters(),lr=0.03)
print(optimizer)


# #定义几层
# net  = nn.Sequential(
#     #定义了两层
#     nn.Linear(num_inputs,5),
#
#     nn.Linear(5,1)
# )

num_epochs=3
for epoch in range(1,num_epochs+1):
    #在每一次迭代中会使用训练数据集中的所有央行本一次
    for x ,y in data_iter(batch_size,feature,label):
        output =net(x)
        l =loss(output,y.view(-1,1))#l是有关小批量x和y的损失
        optimizer.zero_grad()
        # 梯度清零
        l.backward()#接收梯度反传
        optimizer.step()


    #%d按照整数类型输出,     %()格式化运算符
    print('epoch %d ,loss %f'%(epoch,l.item()))
####################################################################################################

#运行
dense =net.linear#这是由于不使用Sequential所以没有角标
print(true_w,dense.weight)
print(true_b,dense.bias)