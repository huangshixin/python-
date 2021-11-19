import numpy as np

a= np.array([1,2,3])
b=np.array([3,4,5])
#进行向量的计算
'''dot时不考虑具体时行向量还是列向量'''
print(a.dot(b))


#计算矩阵的数乘
'''如果输入到multiply中的列表没有做转置操作 则输出一个列表'''
weight =np.array([1,5,2])
values = np.array([1,3,10])
result = np.multiply(weight,values)
print(result)



'''行向量变成列向量   使用新的方式计算有一个矩阵'''

a=np.array(([1,2,3]))
b=np.transpose([a]) #修改b，不会对a进行修改
# b=np.array([a]).T#修改b，不会对a进行修改
c=values*b
print(b)
print(c)
'''
[[ 1  3 10]
 [ 2  6 20]
 [ 3  9 30]]
'''
m = np.multiply(values,b)
print('##########')
print(m
      )

'''
列向量b乘以行向量a

    np.multiply(a,b)

    np.multiply(b,a)

    a*b

    b*a

    np.outer(a,b)

    np.outer(b,a)

    b@a会报错

5、行向量a乘以列向量b

    a@b

'''

'''列向量变行向量'''
a=np.array([[2],[4],[8]])
b=np.transpose(a)#修改b，会对a进行修改
print(b)
