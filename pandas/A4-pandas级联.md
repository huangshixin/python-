          pandas的汇总
          pd.concat   pd.append
          pd.merge     pd.join


【0 回顾numpy的链接】

        a = np.ones((3,4))
        b = np.random.randint((2,4))
    
        np.concate((a,b)，axis=0) ----可以连接【按照行】
         np.concate((a,b)，axis=1) ----不可以连接【按照列】------因为按照列上，维度不一致；
        
        
【1 pandas的级联方式】

        （1） 在维度不同情况下 仍然可以连接
        （2)   

        c = pd.DataFrame(data=np.random.randint(0,100,size=(3,3)),index =list('abc'),columns=list('ABC'))
        d = pd.DataFrame(data=np.random.randint(0,100,size=(3,3)),index =list('abc'),columns=list('DEF'))

        合并操作
        pd.concat((c,d),axis=0)默认是0  需要存入列表 or 元组  0表示纵向连接
         eg： 以下两个纵向连接
          -----
          -----

          -----
          -----
          -----
    
eg：行连接

![image](https://user-images.githubusercontent.com/38878365/192210934-8a71d97a-a797-425a-9b2b-fcf476f4ca82.png)
    
 
 
![image](https://user-images.githubusercontent.com/38878365/192211372-39413a4d-fc5e-4dc2-b600-040e84bc90f0.png)
                                              
![image](https://user-images.githubusercontent.com/38878365/192211464-215f7c94-6682-4a22-8156-c41849e7d916.png)

此时，如果两张表在纵向上合并，且索引无意义，那么可以使用ignore_index=True

![image](https://user-images.githubusercontent.com/38878365/192211975-5ad31662-f0d5-4e46-9e9e-0588290893ce.png)


使用keys = ['第一季度','第二季度'] 做成多层级索引；在连接的时候，原始索引不能忽略，就可以做成多层级索引；

![image](https://user-images.githubusercontent.com/38878365/192212549-3e669bf2-bdbb-4fc6-941b-c0ef82e37b6a.png)



练习:

1、级联的应用场景
    
    两张表具有相同的字段，且代表不同的含义，比如 第一节度和第二季度的表数据销售额 可以做一个级联
    
    






  
  
