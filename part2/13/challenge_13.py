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
    def __init__(self, length):
        self.length = length

    def calculate_perimeter(self):
        """
        外周の長さを返します
        """
        return self.length * 4

    def change_size(self, change_len):
        """
        引数の分長さを足します、0以下になる場合、変更されません。
        どのぐらい長さを変更したか、メッセージを返します。
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

rectangle1 = Rectangle(3, 6)
square1 = Square(5)
rectangle1.print_info()
square1.print_info()
print(square1.change_size(3))
square1.print_info()
print(rectangle1.what_am_i())
print(square1.what_am_i())
