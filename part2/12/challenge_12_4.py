class Hexagon:
    def __init__(self, length):
        self.length = length

    def calculate_perimeter(self):
        """
        外周の長さを計算して返します。
        """
        return self.length * 6

hexagon1 = Hexagon(5)
print("この六角形の外周の長さは、{}cmです。".format(hexagon1.calculate_perimeter()))
