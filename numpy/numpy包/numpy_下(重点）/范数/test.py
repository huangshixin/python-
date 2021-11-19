import numpy as np
LIST=[]
np.random.seed(45674)
for  i in range(36):
    LIST.append(np.random.choice(40))
#构造形状
new_matrix = np.array(LIST).reshape((6,-1))
print(new_matrix)
#使用洗牌的方法
np.random.shuffle(new_matrix)
print(new_matrix)

a_inverse = np.linalg.inv(new_matrix)
print(a_inverse)
# print(np.random.uniform(2))#输出一个在范围内的值 （low，high，size）

