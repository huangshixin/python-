import torch
'''
1、卷积操作是从右向左 从下到上开始扫描的

2、互相关（cross-relation）是相反的

总结：在我们的运算当中 一般指的是互相关矩阵的计算
'''



from torch import  nn
'''下面我们将上述过程实现在corr2d函数里。它接受输入数组X与核数组K，并输出数组Y'''



def corr2d(x,k):
    '''
    卷积操作----------思考怎么利用矩阵
    :param x: 像素矩阵
    :param k: 卷积核filter
    :return:
    '''
    h,w =k.shape
    Y = torch.zeros((x.shape[0]-h+1,x.shape[1]-w+1))#计算卷积后的feature map的形状大小----提前赋予初值 为0
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            '''在原来的基础上加上卷积核的长度和宽度'''
            Y[i,j]=(x[i:i+h,j:j+w]*k).sum()
    return Y

X = torch.tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
K = torch.tensor([[0, 1], [2, 3]])
print(corr2d(X, K))




#二维卷积层
class Conv2D(nn.Module):
    def __init__(self, kernel_size):
        super(Conv2D, self).__init__()
        #s随机生成一个权重（filter）和一个偏差
        self.weight = nn.Parameter(torch.randn(kernel_size))
        self.bias = nn.Parameter(torch.randn(1))

    def forward(self, x):
        return corr2d(x, self.weight) + self.bias



#图像中问题边缘检测
X = torch.ones(6, 8)#6x8矩阵
X[:, 2:6] = 0#第3列到第6列为0，其余为1
print(X)
'''
tensor([[1., 1., 0., 0., 0., 0., 1., 1.],
        [1., 1., 0., 0., 0., 0., 1., 1.],
        [1., 1., 0., 0., 0., 0., 1., 1.],
        [1., 1., 0., 0., 0., 0., 1., 1.],
        [1., 1., 0., 0., 0., 0., 1., 1.],
        [1., 1., 0., 0., 0., 0., 1., 1.]])
'''
K = torch.tensor([[1, -1]])#tensor就是矩阵形式

print('计算自定义矩阵中的元素检测下面将输入X和我们设计的卷积核K做互相关运算。可以看出，我们将从白到黑的边缘和从黑到白的边缘分别检测成了1和-1。其余部分的输出全是0。\n')
print(corr2d(X,K))



Y = corr2d(X, K)#通过卷积得到的特征映射

'''我想学习一下卷积核的大小'''
# 构造一个核数组形状是(1, 2)的二维卷积层
conv2d = Conv2D(kernel_size=(1, 2))#随机生成权重和偏置
print(conv2d(X))#Conv2D ---默认梯度反传、定义kernel大小 随机生成weight 和 bias 最后返回一个矩阵




step =20
lr =0.01
for i in range(step):
    Y_hat =conv2d(X)# X是矩阵
    l= ((Y_hat-Y)**2).sum()#各个位置的差的平方之和
    l.backward()

    # #梯度下降
    conv2d.weight.data -=lr*conv2d.weight.grad
    conv2d.bias.data -= lr * conv2d.bias.grad

    #梯度清零 fill_0(0)
    conv2d.weight.grad.fill_(0)
    conv2d.bias.grad.fill_(0)
    if (i+1)%5 ==0:
        '''表达式   step  %d
        1、%d表示按整型数据的实际长度输出数据。

        2、%c用来输出一个字符。

        3、%s用来输出一个字符串。

        4、%x表示以十六进制数形式输出整数。
         '''
        print('step %d ,loss %d' %(i+1,l.item()))
print("weight: ", conv2d.weight.data)
print("bias: ", conv2d.bias.data)








