#numpy array 提供了运算基础

1、Series 是一种类似于一维数组的对象，由下面两个部分组成；
    value :一组数据（ndarray类型）
    index： 相关数据索引标签

Pandas 的主要数据结构是 Series （一维数据）与 DataFrame（二维数据），这两种数据结构足以处理金融、统计、社会科学、工程等领域里的大多数典型用例。

Pandas Series 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型。

    【作用】
    1、你可以将它理解为强化后的【列表】、以及字典
    2、它具备和【字典】一样的索引方式，同时也具备和列表一样的索引方式 ；索引值为0开始
    3、在API当中，data是传入的列表的值，【index可以是列表的值，但必须与data的长度是匹配的】；-------------【相当于给data中的每一个元素，赋值了一个索引标记】
    4、dtype会自动的寻找【数据类型】
    5、【这里的创建是’引用‘】---也就是说，当创建的Series被改变的时候，原始地址的值也会发生改变；------但是你可以使用copy=True；这样就创建了副本
    '''

    Series 由索引（index）和列组成，函数如下：

    pandas.Series( data, index, dtype, name, copy)

    参数说明：

        data：一组数据(ndarray 类型)。

        index：数据索引标签，如果不指定，默认从 0 开始。

        dtype：数据类型，默认会自己判断。

        name：设置名称。

        copy：拷贝数据，默认为 False。

    '''    
    
import pandas as pd

a = ["Google", "Runoob", "Wiki"]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)   
    
  
  
当输入的data是【字典】类型的时候，此时index的长度可以【不等于】data的长度，但是在输出的时候只会选择具有固定索引长度的值【当data为  “字典” 时候 ，目的是查找，而不是修改】
    sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
    print(pd.Series(sites,index=[1,2]))
    
    dtype: int64
    1    Google
    2    Runoob
    dtype: object
