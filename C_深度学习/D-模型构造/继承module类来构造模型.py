import  torch
from  torch import  nn

#继承Module类来构造模型
'''
Module类使nn模块里提供的模型构造类，使所有神经网络模块的基类
'''

class MLP(nn.Module):

    def __init__(self,**kwargs):
        # 调用MLP父类Module的构造函数来进行必要的初始化。这样在构造实例时还可以指定其他函数
        # 参数，如“模型参数的访问、初始化和共享”一节将介绍的模型参数params
        super(MLP, self).__init__(**kwargs)
        self.hidden = nn.Linear(784, 256)  # 隐藏层
        self.act = nn.ReLU()
        self.output = nn.Linear(256, 10)  # 输出层

    def forward(self,x):

        #以上的MLP类中无须定义反向传播函数。系统将通过自动求梯度而自动生成反向传播所需的backward函数。
        print(x)
        hidden_layer =self.hidden(x)
        fun_1 = self.act(hidden_layer)
        output_layer =self.output(fun_1)
        return output_layer

x_layer = torch.rand(2, 784)
net = MLP()
print(net.forward(x_layer))
# print(net(X))



