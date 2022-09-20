numpy 聚合 
sum（） 
mean（） 
median()

1、series和一个数计算
【符合广播机制】
 s =Series(data=np.random.randint(0,10,size=5),index=lisT("ABCDE"))
 print(s+4)  ---系统会默认广播机制



2、series和一个numpy计算
n = np.ones(shape=5)
print(s+n)---隐式索引对其



3、
add() +
sub() -
mul() *
div() /


