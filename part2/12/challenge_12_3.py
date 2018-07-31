class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        面積を求めて返します。
        """
        return self.width * self.height / 2

    def print_info(self):
        """
        インスタンスの情報を表示します。
        """
        print("この三角形の横は{}cmで、高さは{}です。".format(self.width, self.height))
        print("また、面積は{}㎠です。".format(self.area()))

triangle1 = Triangle(3, 5)
triangle1.print_info()
