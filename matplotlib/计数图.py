import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
'''
避免点重叠问题的另一个选择是增加点的大小，这取决于该点中有多少点。 因此，点的大小越大，其周围的点的集中度越高。
groupby操作涉及拆分对象，应用函数和组合结果的某种组合。这可用于对这些组上的大量数据和计算操作进行分组。
reset_index重置DataFrame的索引，并使用默认值。如果DataFrame具有MultiIndex，则此方法可以删除一个或多个级别
'''

df = pd.read_csv('../data/mpg_ggplot2.csv')
df_counts = df.groupby(['hwy', 'cty']).size().reset_index(name='counts')

# Draw Stripplot
fig, ax = plt.subplots(figsize=(16, 10), dpi=80)

# sns.stripplot(df_counts.cty, df_counts.hwy, size=df_counts.counts*2, ax=ax)
sns.stripplot(df_counts.cty, df_counts.hwy, ax=ax)

# Decorations
plt.title('Counts Plot - Size of circle is bigger as more points overlap', fontsize=22)
plt.show()







