import pygal
from python入门到实践.B_die import  Die

#玩个游戏创建两个D6的骰子

die_1 =Die()
die_2 =Die()
results = []
for roll_num in range(1000):
    abc =die_1.roll()+die_2.roll()#就是die类当中返回1——6之间的随机数字,每次都需要调用 需要100次
    #for循环里面肯定先查找并且使用内部的重名变量
    results.append(abc)

frequencies = []
max_result =die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):#因为两个骰子的和最小是1 最大是12 而range（1，12）只能到1，11，所以末尾需要加一
    frequency =results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.titile = "Result of rolling one D6 dice 1000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title ="Result"
hist.y_title ="Frequency of Result"

hist.add('D6+D6',frequencies)

hist.render_to_file('dice_visual.svg')