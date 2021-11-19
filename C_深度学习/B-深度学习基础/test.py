import time
import torch
from torch import nn, optim
from torch.utils.data import Dataset, DataLoader
import torchvision
from PIL import Image

import sys
sys.path.append("D:\2_Code_installation\3_Anaconda\Lib") # 为了导入上层目录的d2lzh_pytorch
import d2lzh_pytorch as d2l
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


torch.utils.data.DataLoader()#用该语句进行数据集的加载
