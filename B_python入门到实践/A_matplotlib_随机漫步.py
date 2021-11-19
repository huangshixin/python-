import matplotlib.pyplot as plt
from python入门到实践.random_walk import  RandonmWalk

rw = RandonmWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show()

