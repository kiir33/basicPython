import math
class Shape:
    def __init__(self):
        self.color = "red"
        self.sides = 0

    def calArea(self):
        return 0

class Square(Shape):
    def __init__(self,w,c):
        Shape.__init__(self)
        self.width = w
        self.color = c

class Circle(Shape):
    def __init__(self,r,c):
        Shape.__init__(self)
        self.radius = r
        self.color = c

sq1 = Square(5, "Green")
sq2= Square(9, "Black")
c1 = Circle(3,"Orange")

print("Square size", sq1.width, "X", sq1.sides, sq1.color,",",sq2.width,"X",sq2.sides,sq2.color)
print("Circle", c1.radius,c1.color)

print(sq1.calArea())
print(c1.calArea())