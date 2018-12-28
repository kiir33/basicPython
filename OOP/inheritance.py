import math
class Square:
    def __init__(self):
        self.color = "red"
        self.sides = 4
        self.area = 16
    def description(self):
        print("%s Square of side %s and area %s" % (self.color, self.sides, self.area))

sq1 = Square()
sq1.description()