基本概念（常用的一些方法）

1、shape：查看形状，维度
2、size查看大小
3、index查看索引标记
4、values：当前值

s=Series(data=[102,3,2,32,232,10],index=[与data长度匹配])
#比如你是一个Series对象
s.index 返回其中的索引值，一般是显式索引
s.index =='语文' 



5、head（2） 在头切几个 ，可以传入具体的int数据
6、tail（6）在尾部切几个



【当索引没有对应的值时候，可能出现缺失数据显式NaN】
s = Series(data=dict(字典),index = [具体的索引值])

【当给定的索引在其中额时候，打印s会将其打印出来，如果不存在则返回NaN】



#判断
7、pd.isnull()在Serise中自带的 ，判断某一个~~~~~index是否存在【空值】
8、pd.notnull()  如果没有空值，则返回True   notnull().all()





#根据值排序
s.sort_values(ascending=False) 默认是True 表示升序排列


#根据索引排序

s.sort_indx(ascending=True)

#统计值出现的次数
[
通常的设计需求可能是：
  给定一张csv或者excel文件，然后使用pd进行read_csv读取
  之后，使用Series--对某一列属性进行获取
  紧接着，使用value_counts()去统计该属性中出现的【个数】
  
  【系统会默认打印出，dtype类型】
]
s.value_counts()
