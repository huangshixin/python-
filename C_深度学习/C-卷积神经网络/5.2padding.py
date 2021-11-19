import torch
'''

长度; [（原图高 - 卷积核高 +2padding）/stride ]+1 

宽度：[（原图宽 - 卷积核宽 +2padding）/stride ]+1 

实验中 一般我们会把2padding设置为 ----卷积核宽/高-1 （特别是步长为1）
假设这里khkh​是奇数，我们会在高的两侧分别填充ph/2ph​/2行。如果khkh​是偶数，一种可能是在输入的顶端一侧填充⌈ph/2⌉⌈ph​/2⌉行，而在底端一侧填充⌊ph/2⌋⌊ph​/2⌋行。在宽的两侧填充同理。
'''


#这一部分的代码 需要5.1部分才能执行
from torch import nn

# 定义一个函数来计算卷积层。它对输入和输出做相应的升维和降维
def comp_conv2d(conv2d, X):
    # (1, 1)代表批量大小和通道数（“多输入通道和多输出通道”一节将介绍）均为1
    X = X.view((1, 1) + X.shape)
    Y = conv2d(X)
    return Y.view(Y.shape[2:])  # 排除不关心的前两维：批量和通道

# 注意这里是两侧分别填充1行或列，所以在两侧一共填充2行或列
conv2d = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=3, padding=1)

X = torch.rand(8, 8)
comp_conv2d(conv2d, X).shape


# 使用高为5、宽为3的卷积核。在高和宽两侧的填充数分别为2和1
conv2d = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=(5, 3), padding=(2, 1))
comp_conv2d(conv2d, X).shape

#*****************************************************************************************
conv2d = nn.Conv2d(1, 1, kernel_size=(3, 5), padding=(0, 1), stride=(3, 4))
comp_conv2d(conv2d, X).shape