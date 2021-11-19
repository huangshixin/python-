import torch
from torch import nn
from torch.nn import init
import numpy as np
import sys
# sys.path.append("..")
import d2lzh as d2l
from torch.utils.data import DataLoader
from torchvision.datasets import FashionMNIST
from torchvision import transforms

num_inputs,num_hiddens,num_outputs =784,256,10


class FlattenLayer(nn.Module):
    def __init__(self):
        super(FlattenLayer, self).__init__()
    def forward(self, x): # x shape: (batch, *, *, ...)
        return x.view(x.shape[0], -1)

net =nn.Sequential(

    FlattenLayer(),
    nn.Linear(num_inputs,num_hiddens),
    nn.ReLU(),
    nn.Linear(num_hiddens,num_outputs)#全连接操作
)

for params in net.parameters():
    #获取训练中的每一组的参数
    init.normal_(params,mean=0,std=0.01)#初始化 设置均值为0 随机梯度下降的学习了为0.01



root_train =r'D:\4_data\1_DataSet\Minist\FashionMNIST\FashionMNIST\raw\train-images-idx3-ubyte.gz'
root_test =r'D:\4_data\1_DataSet\Minist\FashionMNIST\FashionMNIST\raw\t10k-images-idx3-ubyte.gz'

batch_size =256
mnist_train =FashionMNIST(root=r'D:\4_data\1_DataSet\Minist\FashionMNIST',train=True, download=False, transform=transforms.ToTensor())
mnist_test = FashionMNIST(root=r'D:\4_data\1_DataSet\Minist\FashionMNIST',train=False, download=False, transform=transforms.ToTensor())


train_iter =DataLoader(mnist_train,batch_size=256,shuffle=True)
test_iter =DataLoader(mnist_test,batch_size=256,shuffle=False)

loss =torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), lr=0.5)
num_epochs = 5
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size, None, None, optimizer)
