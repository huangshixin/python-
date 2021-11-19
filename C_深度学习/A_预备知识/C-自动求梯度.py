import  torch

'''
上一节介绍的Tensor是这个包的核心类，如果将其属性.requires_grad设置为True，它将开始追踪(track)在其上的所有操作

（这样就可以利用链式法则进行梯度传播了）。

完成计算后，可以调用.backward()来完成所有梯度计算。此Tensor的梯度将累积到.grad属性中。

.requires_grad=True#则开始追踪其上的所有操作

。backward（）开始完成所有梯度计算

tensor的梯度将累计到.grad属性中

如果不想要被继续追踪，可以调用.detach()将其从追踪记录中分离出来，这样就可以防止将来的计算被追踪，

这样梯度就传不过去了。此外，还可以用with torch.no_grad()将不想被追踪的操作代码块包裹起来，

这种方法在评估模型的时候很常用，因为在评估模型时，我们并不需要计算可训练参数（requires_grad=True）的梯度。
'''

#创建一个Tensor并设置requires_grad=True
x=torch.ones(2,2,requires_grad=True)
print(x)
print(x.grad_fn) #则grad_fn返回一个与这些        <<<<运算>>>>>       相关的对象， 否则是None。

'''
tensor([[1., 1.],
        [1., 1.]], requires_grad=True)
None
'''





#再做一下运算操作：
y = x + 2
print(y)
print(y.grad_fn)
"""
tensor([[3., 3.],
        [3., 3.]], grad_fn=<AddBackward>)
<AddBackward object at 0x1100477b8>
"""


#复杂的操作
z = y * y * 3
out = z.mean()
print(out,end='\n')#tensor(27., grad_fn=<MeanBackward0>)
print(z, out)



#.requires_grad_()来用in-place的方式改变
print("\n")
a = torch.randn(2, 2) # 缺失情况下默认 requires_grad = False
a = ((a * 3) / (a - 1))
print("\n")
print(a)
print(a.requires_grad) # False
a.requires_grad_(True)
print(a.requires_grad) # True
b = (a * a).sum()
print(b.grad_fn)




"""
_____________________________________________________________________________________________________________
梯度
_____________________________________________________________________________________________________________
"""
print("*********************************************************")
out.backward() # 等价于 out.backward(torch.tensor(1.))

print(x.grad)#输出的out关于x的梯度

# 再来反向传播一次，注意grad是累加的
out2 = x.sum()
out2.backward()
print(x.grad)

out3 = x.sum()
x.grad.data.zero_()
out3.backward()
print(x.grad)

x = torch.tensor([1.0, 2.0, 3.0, 4.0], requires_grad=True)
y = 2 * x
z = y.view(2, 2)
print(z)


v = torch.tensor([[1.0, 0.1], [0.01, 0.001]], dtype=torch.float)
z.backward(v)
print(x.grad)





'''再来看看中断梯度追踪的例子'''

x = torch.tensor(1.0, requires_grad=True)
y1 = x ** 2
with torch.no_grad():
    y2 = x ** 3
y3 = y1 + y2

print(x.requires_grad)
print(y1, y1.requires_grad) # True
print(y2, y2.requires_grad) # False
print(y3, y3.requires_grad) # True

y3.backward()
print(x.grad)


x = torch.ones(1,requires_grad=True)

print(x.data) # 还是一个tensor
print(x.data.requires_grad) # 但是已经是独立于计算图之外

y = 2 * x
x.data *= 100 # 只改变了值，不会记录在计算图，所以不会影响梯度传播

y.backward()
print(x) # 更改data的值也会影响tensor的值
print(x.grad)




# 以下代码只有在PyTorch GPU版本上才会执行
if torch.cuda.is_available():
    device = torch.device("cuda")          # GPU
    y = torch.ones_like(x, device=device)  # 直接创建一个在GPU上的Tensor
    x = x.to(device)                       # 等价于 .to("cuda")
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))       # to()还可以同时更改数据类型