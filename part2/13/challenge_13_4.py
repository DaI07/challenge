class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

    def print_info(self):
        print("馬の名前は、{}で、騎手の名前は、{}です。".format(self.name, self.rider.name))

class Rider:
    def __init__(self, name):
        self.name = name

rider1 = Rider("bob")
horse1 = Horse("Jon", rider1)
horse1.print_info()
