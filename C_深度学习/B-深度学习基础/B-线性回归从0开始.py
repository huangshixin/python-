import torch
import numpy as np
import random
import matplotlib.pyplot as plt
from IPython import display
'''
y=wx+b+t(t是一个噪声项）它服从均值为0，标准差为0，01的正太分布
'''
#随机生成一个1000数据 两列的矩阵'''
num_inputs =2
num_examples =1000
true_w =[2,-3.4]
true_b =4.2
feature =torch.randn(num_examples,num_inputs,dtype=torch.float32)
'''features的每一行是一个长度为2的向量，而labels的每一行是一个长度为1的向量（标量）。 这个和随机数里面是有区别的'''
# print(type(feature))#<class 'torch.Tensor'>
# print(np.shape(feature))#torch.Size([1000, 2])
label =true_w[0]*feature[:,0]+true_w[1]*feature[:,1]+true_b#feature是1000x2，但每一行虽然长度为2 但是值是随机的
label +=torch.tensor(np.random.normal(0,0.01,size=label.size()),dtype=torch.float32)#那个t
# print(feature)
print(feature[0], label[0])








#通过生成的第二个特征feature和标签的散点图
def use_svg_display():
    # 用矢量图显示
    display.set_matplotlib_formats('svg')

def set_figsize(figsize=(3.5, 2.5)):
    use_svg_display()
    # 设置图的尺寸
    plt.rcParams['figure.figsize'] = figsize

# # 在../d2lzh_pytorch里面添加上面两个函数后就可以这样导入
# import sys
# sys.path.append("..")
# from d2lzh_pytorch import *

set_figsize()
plt.scatter(feature[:, 1].numpy(), label.numpy(), 1);
plt.show()










#读取数据
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

#
# #读取第一个小批量数据样本（从0 每次10作为跨度）
batch_size =10
for x ,y in data_iter(batch_size,feature,label):
     #返回两个值 还可以用循环接
     print(x,y)
     break

'''
************************************************************************************************************************
'''









#初始化模型的参数
w =torch.tensor(np.random.normal(0,0.01,(num_inputs,1)),dtype=torch.float32)
b= torch.tensor(1,dtype=torch.float32)

w.requires_grad_(requires_grad=True)
b.requires_grad_(requires_grad=True)



#定义模型
def linreg(X,w,b):
    return torch.mm(X,w)+b#mm相当于向量的和矩阵的点积




#定义损失函数
def squared_loss(y_hat, y):  # 本函数已保存在d2lzh_pytorch包中方便以后使用
    # 注意这里返回的是向量, 另外, pytorch里的MSELoss并没有除以 2
    return (y_hat - y.view(y_hat.size())) ** 2 / 2



#定义优化算法
def SGD(params,lr,batch_size):
    for param in params:
        '''
        grad类似于偏导
        '''
        #param.data是上一次w的权重
        param.data-=lr*param.grad/batch_size # 注意这里更改param时用的param.data




#训练模型
lr = 0.03
num_epochs = 20
net = linreg
loss = squared_loss

for epoch in range(num_epochs):  # 训练模型一共需要num_epochs个迭代周期
    # 在每一个迭代周期中，会使用训练数据集中所有样本一次（假设样本数能够被批量大小整除）。X
    # 和y分别是小批量样本的特征和标签
    for X, y in data_iter(batch_size, feature, label):
        l = loss(net(X, w, b), y).sum()  # l是有关小批量X和y的损失(sum 是所有损失的求和）
        l.backward()  # 小批量的损失对模型参数求梯度
        SGD([w, b], lr, batch_size)  # 使用小批量随机梯度下降迭代模型参数

        # 不要忘了梯度清零
        w.grad.data.zero_()
        b.grad.data.zero_()
    train_l = loss(net(feature, w, b), label)
    print('epoch %d, loss %f' % (epoch + 1, train_l.mean().item()))


print(true_w, '\n', w)
print(true_b, '\n', b)








