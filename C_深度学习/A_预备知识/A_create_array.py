import numpy as np
import torch
from IPython import display
from matplotlib import pyplot as plt
import random
'''
****************************************************************************************
测试cpu运行速度和gpu运行速度
****************************************************************************************
'''
from time import time
a = np.ones(shape=1000)
b = np.ones(shape=1000)

start =time()#向量相加的一种方法是，将这两个向量按元素逐一做标量加法
c= np.zeros(shape=1000)
for i in range(1000):#【0~999】
    c[i] = a[i]+b[i]
print(time() - start)
#向量相加的另一种方法是，将这两个向量直接做矢量加法
start = time()
d = a + b
print(time() - start)



'''
****************************************************************************************
我们构造一个简单的人工训练数据集，它可以使我们能够直观比较学到的参数和真实的模型参数的区别。设训练数据集样本数为1000，
输入个数（特征数）为2。给定随机生成的批量样本特征X2R10002，我们使用线性回归模型真实权重w= [2;
****************************************************************************************
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





def use_svg_display():
    # 用矢量图显示
    display.set_matplotlib_formats('svg')

def set_figsize(figsize=(3.5, 2.5)):
    use_svg_display()
    # 设置图的尺寸
    plt.rcParams['figure.figsize'] = figsize
set_figsize()
plt.scatter(feature[:, 1].numpy(), label.numpy(), 1)  # 加分号只显示图
plt.show()









'''
________________________________________________________________________________________________________________________________________
读取数据集
在训练模型的时候，我们需要遍历数据集并不断读取小批量数据样本。这里我们定义一个函数：它每次返回batch_size（批量大小）个随机样本的特征和标签。
________________________________________________________________________________________________________________________________________
'''

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


#读取第一个小批量数据样本
batch_size =10
for x ,y in data_iter(batch_size,feature,label):
     #返回两个值 还可以用循环接
     print(x,y)
     break













#初始化权重参数parameter
'''
________________________________________________________________________________________________________________________________________
一般来讲权重矩阵是K个N维向量。从直觉上来讲，如果这K个N维向量在N维空间中均匀分布在以原点为中心的N-1维单位超球面上，在随机性上应该是最好的。因为这样，这K个向量的夹角为均匀分布。

此时问题变成了，如何在N-1维超球面上进行均匀采样。根据这篇论文A note on a method for generating points uniformly on n-dimensional spheres 可知，若对N维向量的

每个分量进行N(0,1)的正态分布采样，生成K个N维向量，然后投影到单位超球面上，那么形成的K个N维向量在单位超球面上均匀分布。
________________________________________________________________________________________________________________________________________
'''
w = torch.tensor(np.random.normal(0,0.01,(num_inputs,1)),dtype=torch.float32)
b = torch.zeros(1,dtype=torch.float32)

# save_weight =[0.1,0.2,0.3,0.25]
# loaded_weights = torch.tensor(save_weight)
# print(loaded_weights)
#
# # Now ,start to record operations done to weights
# loaded_weights.requires_grad_()
# #设置这些参数是接收梯度的
w.requires_grad_()
b.requires_grad_()


#定义我们的模型
def linreg(x,w,b):

    #mm等价于 np.multipy乘法运算
    return torch.mm(x,w)+b

#定义损失函数
def squared_loss(y_hat,y):

    #size判断数组  或者矩阵中的元素个数 size（b，axis=）  b是矩阵或者数组 axis是维度
    return (y_hat-y.view(y_hat.size()))**2/2


#优化算法
def SGD(params ,lr,batch_size):
    for param in params:
        param.data -=lr*param.grad/batch_size


#超参手动设置
lr = 0.03
num_epochs =5
net =linreg#我们的model
loss_function =squared_loss

for epoch in range(num_epochs):
    #在每一次迭代中会使用训练数据集中的所有央行本一次
    for x ,y in data_iter(batch_size ,feature,label):
        l =loss_function(net(x,w,b),y).sum()#l是有关小批量x和y的损失
        l.backward()#接收梯度反传
        SGD([w,b],lr,batch_size)#使用小批量随机梯度优化

        #不要忘记梯度清零
        w.grad.data.zero_()
        b.grad.data.zero_()
    train_1 =loss_function(net(feature,w,b),label)
    #%d按照整数类型输出,     %()格式化运算符
    print('epoch %d ,loss %f'%(epoch+1,train_1.mean().item()))

print("*"*30)
print(true_w,'\n',w)
print(true_b,'\n',b)






#查看形状和元素个数
x= torch.arange(12)
x.shape
x.numel()

x=torch.arange(12,dtype=torch.float32).reshape((3,4))
y =torch.tensor([[2.0,1,4,3],[1,2,3,4],[4,5,6,3]])
torch.cat((x,y),dim=0),torch.cat((x,y),dim=1)#0为列 1为行---相加







