class Point:
    def __init__(self, x, y, weight=0, is_barrier=False):
        self.x = x
        self.y = y
        self.cost = 0
        self.parent = None
        self.weight = weight
        self.is_barrier = is_barrier
        self.area_new = self.get_point_area_new()   #增加一个属性表示节点所在的区域, 新区域函数
        self.area_old = self.get_point_area_old()   #增加一个属性表示节点所在的区域， 旧区域函数
        self.color = None
    def get_point_area_new(self):
        """
        根据坐标范围划分不同的区域，并为每个区域分配不同的权重
        """
        if self.x < 10 and self.y < 10:
            return 1+(5-((self.x + self.y) / (9 + 9)))
        elif self.x < 10 and self.y >= 10:
            return 5
        elif self.x >= 10 and self.y < 10:
            return 3
        else:
            return 10

    def get_point_area_old(self):
        """
        根据坐标范围划分不同的区域，并为每个区域分配不同的权重
        """
        # for wheelchair and visually impaired
        # if 0 <= self.x <= 3 and 8 <= self.y <= 12:
        #     return 5
        #
        # elif 1 <= self.x <= 12 and 9 <= self.y <= 17:
        #     return 4
        #
        # elif 12 <= self.x <= 17 and 13 <= self.y <= 17:
        #     return 3
        #
        # elif 19 <= self.x <= 19 and 13 <= self.y <= 18:
        #     return 3
        #
        # elif 1 <= self.x <= 1 and 3 <= self.y <= 7:
        #     return 5
        #
        # else:
        #     return 1

        # for people with hearing impaired
        if 4 <= self.x <= 14 and 9 <= self.y <= 19:
            return 3

        elif 1 <= self.x <= 1 and 2 <= self.y <= 8:
            return 4

        elif 18 <= self.x <= 18 and 14 <= self.y <= 18:
            return 0.2

        else:
            return 1

