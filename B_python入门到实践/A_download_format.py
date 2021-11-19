#16章分析csv中的文件数据

import csv                              # 用于分析CSV文件中的数据行

filename = 'C:\\Users\\huangshixin\\Desktop\sikta_weather_07_2020.csv'
with open(filename) as f:               # 打开文件，并将结果文件对象存储在f中
    reader = csv.reader(f)              # 创建与该文件相关联的阅读器对象，并存储在reader中
    header_row = next(reader)           # 第一行
    print(header_row)                   # 输出显示第一行



"""这里有一些模块待补充"""