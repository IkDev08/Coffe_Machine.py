import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p2):
        d = math.sqrt((float(p2.x) - float(self.x)) ** 2 + (float(p2.y) - float(self.y)) ** 2)
        return d



