import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        面積を求め、小数点第2位になるように偶数の丸めて返します。
        """
        return self.radius * self.radius * math.pi

circle1 = Circle(3)
print("この円の半径は{}cmで、面積は{}㎠です。".format(circle1.radius, round(circle1.area(), 2)))
