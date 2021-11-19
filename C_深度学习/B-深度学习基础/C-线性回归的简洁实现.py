import torch
import numpy as np
from torch import nn

#生成一个数据集
num_inputs = 2
num_examples = 1000
true_w = [2, -3.4]
true_b = 4.2
#生成我们的数据集 1000个
features = torch.tensor(np.random.normal(0, 1, (num_examples, num_inputs)), dtype=torch.float)
#计算该预测的函数值
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
#加上噪声项
labels += torch.tensor(np.random.normal(0, 0.01, size=labels.size()), dtype=torch.float)


import torch.utils.data as Data

batch_size = 10
# 将训练数据的特征和标签组合
dataset = Data.TensorDataset(features, labels)

# 随机读取小批量
data_iter = Data.DataLoader(dataset, batch_size, shuffle=True)

#读取并打印一个小批量数据
for X, y in data_iter:
    print(X, y)
    break


#定义模型
class LinearNet(nn.Module):
    def __init__(self, n_feature):
        super(LinearNet, self).__init__()
        self.linear = nn.Linear(n_feature, 1)#线性分类器的特征有两个
    # forward 定义前向传播
    def forward(self, x):#这个x是你的图片或者其他的东西 -----向量
        y = self.linear(x)
        return y

net = LinearNet(num_inputs)
print(net) # 使用print可以打印出网络的结构




#我们可以通过net.parameters()来查看模型中所有可学习的参数
for param in net.parameters():
    print(param)
'''
torch.nn仅支持输入一个batch的样本不支持单个样本输入，如果只有单个样本，可使用input.unsqueeze(0)来添加一维
'''



#初始化模型参数
from torch.nn import init
'''
normal将权重参数每个元素初始化为随机采样于均值为0、标准差为0。01的正太分布
'''
init.normal_(net.linear.weight, mean=0, std=0.01)
init.constant_(net.linear.bias, val=0)  # 也可以直接修改bias的data: net[0].bias.data.fill_(0)



loss = nn.MSELoss()



#优化器
import torch.optim as optim

optimizer = optim.SGD(net.parameters(), lr=0.03)
print(optimizer)
'''
SGD (
Parameter Group 0
    dampening: 0
    lr: 0.03
    momentum: 0
    nesterov: False
    weight_decay: 0
)
如何调整学习率
optimizer.param_groups
'''
# 调整学习率
for param_group in optimizer.param_groups:
    param_group['lr'] *= 0.1 # 学习率为之前的0.1倍





#训练模型
num_epochs = 3
for epoch in range(1, num_epochs + 1):
    for X, y in data_iter:
        output = net(X)
        l = loss(output, y.view(-1, 1))
        optimizer.zero_grad() # 梯度清零，等价于net.zero_grad()
        l.backward()
        optimizer.step()
    print('epoch %d, loss: %f' % (epoch, l.item()))

dense = net.linear
print(dense)
print("*****************************\n")
print(true_w, dense.weight)
print(true_b, dense.bias)









