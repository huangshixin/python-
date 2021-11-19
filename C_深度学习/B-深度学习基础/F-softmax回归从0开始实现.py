import torch
from torch import nn
from torch.nn import init
from torchvision.datasets import FashionMNIST
import numpy as np
import sys
from torch.utils.data import DataLoader
from torchvision import transforms



'''
1、数据加载
2、权重初始化、数据预处理 分割 裁剪
3、loss函数定义
4、准确度估计


torchvision.datasets: 一些加载数据的函数及常用的数据集接口；

torchvision.models: 包含常用的模型结构(含预训练模型)，例如AlexNet、VGG、ResNet等；

torchvision.transforms: 常用的图片变换，例如裁剪、旋转等；

torchvision.utils: 其他的一些有用的方法


解释方法含义：

1、dataset：提前定义的dataset的实例；
2、batch_size：传入数据的batch大小，常常是32、64、128、256’
3、shuffle：bool类型，表示是否在每次获取数据的时候提前打乱数据；
4、num_workers：加载数据的线程数。
5、drop_last：bool类型，为真，表示最后的数据不足一个batch，就删掉

'''

root_train =r'D:\4_data\1_DataSet\Minist\FashionMNIST\FashionMNIST\raw\train-images-idx3-ubyte.gz'
root_test =r'D:\4_data\1_DataSet\Minist\FashionMNIST\FashionMNIST\raw\t10k-images-idx3-ubyte.gz'


batch_size =256
mnist_train =FashionMNIST(root=r'D:\4_data\1_DataSet\Minist\FashionMNIST',train=True, download=False, transform=transforms.ToTensor())
mnist_test = FashionMNIST(root=r'D:\4_data\1_DataSet\Minist\FashionMNIST',train=False, download=False, transform=transforms.ToTensor())
train_iter =DataLoader(mnist_train,batch_size=256,shuffle=True)
test_iter =DataLoader(mnist_test,batch_size=256,shuffle=False)
# print(train_iter)
# print(test_iter)


#3.6.2 初始化模型参数
num_inputs = 784
num_outputs = 10#10个类

W = torch.tensor(np.random.normal(0, 0.01, (num_inputs, num_outputs)), dtype=torch.float)
b = torch.zeros(num_outputs, dtype=torch.float)#相当于没有偏置

#同之前一样，我们需要模型参数梯度。
W.requires_grad_(requires_grad=True)
b.requires_grad_(requires_grad=True)



X =torch.tensor([[1,2,3],[4,5,6]])
print(X.sum(dim =0,keepdim=True))#dim=0是列  dim=1是行
print(X.sum(dim =1,keepdim=True))



#开始定义softmax运算
'''
我们先描述一下如何对多维的tensor按维度操作
给定一个tensor矩阵x。

我们可以只对其中同一列（dim=0）或者同一行（dim=1）的元素求和，

并在结果中保留行和列这两个维度（keepdim=True）
'''
def softmax(m):
    '''
    输入一个tensor 对每一行的数据做softmax归一化处理
    :param m:
    :return:
    '''
    X_exp =m.exp()# 这是一个矩阵     输入的每一个值都做指数处理
    partition =X_exp.sum(dim=1,keepdim =True)#对行做softmax
    return X_exp/partition#对每一个值做了归一化处理

# X = torch.rand((2, 5))
# X_prob = softmax(X)
# print(X_prob, X_prob.sum(dim=1))






#定义模型（调用softmax算损失）
def net(X):
    return softmax(torch.mm(X.view(-1,num_inputs),W)+b)







#定义损失函数
'''为了得到标签的预测概率 我们使用gather函数

y_hat是在2个样本 在三个类别的预测概率
y是两个样本的实际标签

在代码中，标签类别的离散值是从0开始逐一递增的。
'''
y_hat = torch.tensor([[0.1, 0.3, 0.6], [0.3, 0.2, 0.5]])
y = torch.LongTensor([0, 2])#向量 或者列表
print('\n查看一下功能')
print(y)
y_hat.gather(1, y.view(-1, 1))





#计算分类准确度

'''
给定一个类别的-----预测概率分布y-hat ------我们把预测概率-----------最大的类别-----------作为输出类别
如果预测的值和真实值一致 则说明预测正确 否则预测错误


----
其中y_hat.argmax(dim=1)返回矩阵y_hat每行中最大元素的索引，且返回结果与变量y形状相同。argmax返回最大值index
----
相等条件判断式(y_hat.argmax(dim=1) == y)是一个类型为ByteTensor的Tensor，我们用float()将其转换为值为0（相等为假）或1（相等为真）的浮点型Tensor
'''
def accuracy(y_hat, y):
    return (y_hat.argmax(dim=1) == y).float().mean().item()
print(accuracy(y_hat, y))


# 本函数已保存在d2lzh_pytorch包中方便以后使用。该函数将被逐步改进：它的完整实现将在“图像增广”一节中描述
def evaluate_accuracy(data_iter, net):
    acc_sum, n = 0.0, 0
    for X, y in data_iter:
        acc_sum += (net(X).argmax(dim=1) == y).float().sum().item()
        n += y.shape[0]
    return acc_sum / n

print(evaluate_accuracy(test_iter, net))





# num_epochs, lr = 5, 0.1
#
# # 本函数已保存在d2lzh包中方便以后使用
# def train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size,
#               params=None, lr=None, optimizer=None):
#     for epoch in range(num_epochs):
#         train_l_sum, train_acc_sum, n = 0.0, 0.0, 0
#         for X, y in train_iter:
#             y_hat = net(X)
#             l = loss(y_hat, y).sum()
#
#             # 梯度清零
#             if optimizer is not None:
#                 optimizer.zero_grad()
#             elif params is not None and params[0].grad is not None:
#                 for param in params:
#                     param.grad.data.zero_()
#
#             l.backward()
#             if optimizer is None:
#                 d2l.sgd(params, lr, batch_size)
#             else:
#                 optimizer.step()  # “softmax回归的简洁实现”一节将用到
#
#
#             train_l_sum += l.item()
#             train_acc_sum += (y_hat.argmax(dim=1) == y).sum().item()
#             n += y.shape[0]
#         test_acc = evaluate_accuracy(test_iter, net)
#         print('epoch %d, loss %.4f, train acc %.3f, test acc %.3f'
#               % (epoch + 1, train_l_sum / n, train_acc_sum / n, test_acc))
#
# train_ch3(net, train_iter, test_iter, cross_entropy, num_epochs, batch_size, [W, b], lr)



















