from random import choice
class RandonmWalk():
    def __init__(self,num_point=5000):
        """初始化随机漫步包含的所有点"""
        self.num_point=num_point
        self.x_values=[0]
        self.y_values=[0]
        #代表我们从00处出发，我们选择choice
    def fill_walk(self):
        """计算随机漫步包含的所有点,不断漫步知道到达指定的长度"""
        while len(self.x_values) < self.num_point:

            # 决定前进的方向以及沿着这个方向前进的距离
            x_direction = choice([1, -1])  # 向右走的1，向左的走-1
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction

            # 拒绝原地漫步
            if x_step == 0 and y_step == 0:
                continue
            # 计算下一个的x和y   x_step是当前的x的位置，
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)