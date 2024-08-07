"""
Programming Python
Desc: Class notation
All rights reserved Lotus Code Studios Sept 2021
"""


# Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        y = self.y * 2
        x = self.x * 2
        dist = (y - x) * 2
        return dist
    # def grand_distance(self, self.other):
    def __repr__(self):
        pass
    def __str__(self):
        return f"X:{self.x}---Y:{self.y}"

point1 = Point(4, 5)

print(point1.distance())