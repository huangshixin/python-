import torch
import torchvision as tr
import torchvision.transforms as transforms  #导入transformer
import matplotlib.pyplot as plt
import time
import sys
# import  d2lzh as d2l这是mxnet里面的一个  如果用pytorch可以使用IPython
from IPython import display
import numpy as np
'''
-----实验数据集下载方式-----
tr.datasets#一些加载数据的函数及常用的数据集接口
tr.models#包含常用的模型结构 例如alexNEt resnet
tr.transforms#常用的图片变换，例如裁剪  旋转
tr.utils#
另外我们还指定了参数transform = transforms.ToTensor()使所有数据转换为Tensor，如果不进行转换则返回的是PIL图片。
-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''





'''mnist_train、mnist_test都是数据集中的子类，我们可以用len或者角标来获取信息  分别仕6w和1w的样本     10个类别'''
mnist_train = tr.datasets.FashionMNIST(root=r'D:\4_data\1_DataSet\Minist\FashionMNIST', train=True, download=True, transform=transforms.ToTensor())
mnist_test = tr.datasets.FashionMNIST(root=r'D:\4_data\1_DataSet\Minist\FashionMNIST', train=False, download=True, transform=transforms.ToTensor())


#--------------查看数据集类型和长度---------------------
print(type(mnist_train),len(mnist_train),end='\n\n')
print(len(mnist_test),end="以上展示test的数据集的length\n\n")
'''
实验效果：
<class 'torchvision.datasets.mnist.FashionMNIST'>
60000 10000
'''



#-------------------尝试着通过下标访问任意一个样本----------
feature ,label =mnist_train[0]
print(feature.shape,label,end='\n') # Channel x Height x Width
#torch.Size([1, 28, 28]) 9
# 变量feature对应-----高和宽----均为28像素的图像。由于我们使用了transforms.ToTensor()，所以每个像素的数值为[0.0, 1.0]的32位浮点数
#需要注意的是，feature的尺寸是  c h w



#---------------简单介绍一下fashion-mnist数据集---------------
'''
Fashion-MNIST中一共包括了10个类别，分别为t-shirt（T恤）、trouser（裤子）、pullover（套衫）、dress（连衣裙）、
coat（外套）、sandal（凉鞋）、shirt（衬衫）、sneaker（运动鞋）、bag（包）和ankle boot（短靴）。
以下函数可以将数值标签转成相应的文本标签。
'''



# 本函数已保存在d2lzh包中方便以后使用
def get_fashion_mnist_labels(labels):
    text_labels = ['t-shirt', 'trouser', 'pullover', 'dress', 'coat',
                   'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']
    return [text_labels[int(i)] for i in labels] #labels是一个列表，存放的是一堆数字 从0-9



# 本函数已保存在d2lzh包中方便以后使用
def show_fashion_mnist(images, labels):
    display.set_matplotlib_formats()
    # 这里的_表示我们忽略（不使用）的变量
    _, figs = plt.subplots(1, len(images), figsize=(12, 12))
    for f, img, lbl in zip(figs, images, labels):
        f.imshow(img.view((28, 28)).numpy())
        f.set_title(lbl)
        f.axes.get_xaxis().set_visible(False)
        f.axes.get_yaxis().set_visible(False)
    plt.show()


X, y = [], []
for i in range(10):
    X.append(mnist_train[i][0])
    y.append(mnist_train[i][1])
show_fashion_mnist(X, get_fashion_mnist_labels(y))







#读取小批量

batch_size =256
if sys.platform.startswith('win'):
    num_workers =0 #0表示不用额外的进程来加速读取数据
else:
    num_workers =4
train_iter = torch.utils.data.DataLoader(mnist_train, batch_size=batch_size, shuffle=True, num_workers=num_workers)
test_iter = torch.utils.data.DataLoader(mnist_test, batch_size=batch_size, shuffle=False, num_workers=num_workers)

'''我们将获取并读取Fashion-MNIST数据集的逻辑封装在d2lzh_pytorch.load_data_fashion_mnist函数中供后面章节调用。'''

# #该函数将返回train_iter和test_iter两个变量。
start=time.time()
for X,y in train_iter:
    continue
print('%.1 secore'% (time.time()-start),end='\n')