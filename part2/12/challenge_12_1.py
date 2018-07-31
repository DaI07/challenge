class Apple:
    def __init__(self, weight, color, variety, production_area):
        self.weight = weight
        self.color = color
        self.variety = variety
        self.production_area = production_area

    def print_info(self):
        """
        このメソッドはインスタンスの情報を表示します。
        """
        print("このりんごの品種は{}で、産地は、{}です。".format(self.variety, self.production_area))
        print("また、重さは、{}グラムで、色は{}です。".format(self.weight, self.color))

apple1 = Apple("150", "赤", "ふじ", "青森")
apple1.print_info()
