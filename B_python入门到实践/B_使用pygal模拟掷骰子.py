from python入门到实践.B_die import  Die

die =Die()

results = []
for roll_num in range(100):
    abc =die.roll()#就是die类当中返回1——6之间的随机数字,每次都需要调用 需要100次
    #for循环里面肯定先查找并且使用内部的重名变量
    results.append(abc)

#分析结果
requencies = []
for res in range(1,7):
    #obj -- 列表中统计的对象。  count（obj）是统计对象等于obj的个数的
    result_value =results.count(res)
    requencies.append(result_value)

print(requencies)

#[20, 11, 17, 16, 19, 17]