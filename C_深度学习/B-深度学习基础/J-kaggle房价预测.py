import torch
import torch.nn as nn
import numpy as np
import pandas as pd
import sys
import d2lzh as d2l
#conda install --use-local 地址

#[1460 rows x 81 columns]
train_data =pd.read_csv(r'D:\4_data\1_DataSet\3-housePrice\train.csv')
#test_data.shape # 输出 (1459, 80)
test_date =pd.read_csv(r'D:\4_data\1_DataSet\3-housePrice\test.csv')

#提取数据集信息
print(train_data.info())
numer_feature =train_data.select_dtypes(include =[np.number])
print(numer_feature)
categorical_feature =train_data.select_dtypes(include=[np.object])
print(categorical_feature,end='\n***********************************************************\n')

#查看前4个样本的前4个特征 后2个特征和标签（salePrice）-----------房屋信息中的数据有很多

a =train_data.iloc[0:4 ,[0,1,2,3,-3,-2,-1]]#[0,1,2,3,-3,-2,-1]看成是列的展示
#    Id  MSSubClass MSZoning  LotFrontage SaleType SaleCondition  SalePrice
# 0   1          60       RL         65.0       WD        Normal     208500
# 1   2          20       RL         80.0       WD        Normal     181500
# 2   3          60       RL         68.0       WD        Normal     223500
# 3   4          70       RL         60.0       WD       Abnorml     140000
print(a,end='\n')

print(train_data.iloc[:,1:-1],end='\n')


'''可以看到第一个特征是Id，它能帮助模型记住每个训练样本，但难以推广到测试样本，所以我们不使用它来训练,我们将所有的训练数据和测试数据的79个特征按样本连结。'''
all_features = pd.concat((train_data.iloc[:,1:-1],test_date.iloc[:,1:]))




#数据预处理
'''
我们对连续数值的特征做标准化standardization）
我们可以将该特征的每个值先减去μ 再除以σ得到标准化后的每个特征值。对于缺失的特征值，我们将其替换成该特征的均值。
'''

#通过dtype获得 列表、元组元素扽数据类型 ，之后再通过index获得其索引  object被转化为数据类型的对象
numeric_features = all_features.dtypes[all_features.dtypes != 'object'].index
print(all_features.dtypes)

#apply  当一个函数的参数存在于一个元组或者一个字典中时，用来间接的调用这个函数，并将元组或者字典中的参数按照顺序传递给参数
all_features[numeric_features] = all_features[numeric_features].apply(
    lambda x: (x - x.mean()) / (x.std()))
# 标准化后，每个数值特征的均值变为0，所以可以直接用0来替换缺失值(fillna(0)相当于填充的作用
all_features[numeric_features] = all_features[numeric_features].fillna(0)




#离散数值转成指示特征
'''
举个例子，假设特征MSZoning里面有两个不同的离散值RL和RM，那么这一步转换将去掉MSZoning特征，并新加两个特征MSZoning_RL和MSZoning_RM，其值为0或1。
如果一个样本原来在MSZoning里的值为RL，那么有MSZoning_RL=1且MSZoning_RM=0。
'''
# dummy_na=True将缺失值也当作合法的特征值并为其创建指示特征
all_features = pd.get_dummies(all_features, dummy_na=True)
print(all_features.shape) # (2919, 331)#特征转化从79到了331



'''
dtypes
dtype--查数据类型,适用于tensor
type()
shape
size
'''

#最后，通过values属性得到NumPy格式的数据，并转成Tensor方便后面的训练。
n_train = train_data.shape[0]

train_features = torch.tensor(all_features[:n_train].values, dtype=torch.float)

test_features = torch.tensor(all_features[n_train:].values, dtype=torch.float)
train_labels = torch.tensor(train_data.SalePrice.values, dtype=torch.float).view(-1, 1)





#训练模型
loss  =torch.nn.MSELoss()#平方损失

def get_net(feature_num):
    net = nn.Linear(feature_num, 1)#全连接
    for param in net.parameters():
        nn.init.normal_(param, mean=0, std=0.01)
    return  net


#文中使用对数均方根误差
def log_rmse(net, features, labels):
    '''

    :param net:
    :param features:
    :param labels: 实际标签
    :return:
    '''
    with torch.no_grad():
        # 将小于1的值设成1，使得取对数时数值更稳定
        clipped_preds = torch.max(net(features), torch.tensor(1.0))#预测标签
        rmse = torch.sqrt(loss(clipped_preds.log(), labels.log()))#log（yi)-log(y)
    return rmse.item()

def train(net, train_features, train_labels, test_features, test_labels,
          num_epochs, learning_rate, weight_decay, batch_size):
    train_ls, test_ls = [], []
    dataset = torch.utils.data.TensorDataset(train_features, train_labels)
    train_iter = torch.utils.data.DataLoader(dataset, batch_size, shuffle=True)
    # 这里使用了Adam优化算法
    optimizer = torch.optim.Adam(params=net.parameters(), lr=learning_rate, weight_decay=weight_decay)
    net = net.float()
    for epoch in range(num_epochs):
        for X, y in train_iter:
            l = loss(net(X.float()), y.float())
            optimizer.zero_grad()
            l.backward()
            optimizer.step()
        train_ls.append(log_rmse(net, train_features, train_labels))
        if test_labels is not None:
            test_ls.append(log_rmse(net, test_features, test_labels))
    return train_ls, test_ls



'''
    assert语句用来声明某个条件是真的。
    如果你非常确信某个你使用的列表中至少有一个元素，而你想要检验这一点，并且在它非真的时候引发一个错误，那么assert语句是应用在这种情形下的理想语句。
    当assert语句失败的时候，会引发一AssertionError。
    
    if not expression:
    raise AssertionErro
'''
def get_k_fold_data(k, i, X, y):
    # 返回第i折交叉验证时所需要的训练和验证数据
    '''assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假'''
    assert k > 1
    fold_size = X.shape[0] // k#整数除法
    X_train, y_train = None, None
    for j in range(k):
        idx = slice(j * fold_size, (j + 1) * fold_size)
        X_part, y_part = X[idx, :], y[idx]
        if j == i:
            X_valid, y_valid = X_part, y_part
        elif X_train is None:
            X_train, y_train = X_part, y_part
        else:
            X_train = torch.cat((X_train, X_part), dim=0)
            y_train = torch.cat((y_train, y_part), dim=0)
    return X_train, y_train, X_valid, y_valid


def k_fold(k, X_train, y_train, num_epochs,
           learning_rate, weight_decay, batch_size):
    train_l_sum, valid_l_sum = 0, 0
    for i in range(k):
        data = get_k_fold_data(k, i, X_train, y_train)
        net = get_net(X_train.shape[1])
        train_ls, valid_ls = train(net, *data, num_epochs, learning_rate,
                                   weight_decay, batch_size)
        train_l_sum += train_ls[-1]
        valid_l_sum += valid_ls[-1]
        if i == 0:
            d2l.semilogy(range(1, num_epochs + 1), train_ls, 'epochs', 'rmse',
                         range(1, num_epochs + 1), valid_ls,
                         ['train', 'valid'])
        print('fold %d, train rmse %f, valid rmse %f' % (i, train_ls[-1], valid_ls[-1]))
    return train_l_sum / k, valid_l_sum / k

k, num_epochs, lr, weight_decay, batch_size = 5, 100, 5, 0, 64
train_l, valid_l = k_fold(k, train_features, train_labels, num_epochs, lr, weight_decay, batch_size)
print('%d-fold validation: avg train rmse %f, avg valid rmse %f' % (k, train_l, valid_l))

def train_and_pred(train_features, test_features, train_labels, test_data,
                   num_epochs, lr, weight_decay, batch_size):
    net = get_net(train_features.shape[1])
    train_ls, _ = train(net, train_features, train_labels, None, None,
                        num_epochs, lr, weight_decay, batch_size)
    d2l.semilogy(range(1, num_epochs + 1), train_ls, 'epochs', 'rmse')
    print('train rmse %f' % train_ls[-1])
    preds = net(test_features).detach().numpy()
    test_data['SalePrice'] = pd.Series(preds.reshape(1, -1)[0])
    submission = pd.concat([test_data['Id'], test_data['SalePrice']], axis=1)
    submission.to_csv('./submission.csv', index=False)
