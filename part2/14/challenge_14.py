class Shape:
    def what_am_i(self):
        return "I am a shape"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        """
        外周の長さを返します
        """
        return self.width*2 + self.height*2

    def print_info(self):
        """
        情報を表示します
        """
        print("この長方形は、横{}cm,縦{}cmです。".format(self.width, self.height))
        print("外周の長さは、{}cmです。".format(self.calculate_perimeter()))

class Square(Shape):
    square_list = []

    def __init__(self, length):
        self.length = length
        self.square_list.append(self)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.length, self.length, self.length, self.length)

    def calculate_perimeter(self):
        """
        外周の長さを返します
        """
        return self.length * 4

    def change_size(self, change_len):
        """
        長さを変更します。0以下にはできません。
        メッセージを返します。
        """
        if self.length + change_len <= 0:
            return "辺の長さを0以下にはできません。"
        else:
            self.length += change_len
            return "辺の長さを{}cm変更しました。".format(change_len)

    def print_info(self):
        """
        情報を表示します
        """
        print("この正方形は、一辺{}cmです。".format(self.length))
        print("外周の長さは、{}cmです。".format(self.calculate_perimeter()))

    def obj_equal(self, obj1, obj2):
        return obj1 is obj2

square1 = Square(5)
square1_copy = square1
square2 = Square(5)
square1.print_info()
print(square1)
print(square1.obj_equal(square1, square1_copy))
print(square1.obj_equal(square1, square2))
