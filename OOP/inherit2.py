import math
class Shape:
    def __init__(self):
        self.color = "red"
        self.sides = 0

class Square(Shape):
    def __init__(self,w,c):
        Shape.__init__(self)
        self.width = w
        self.color = c

sq1 = Square(5, "Green")
sq2= Square(9, "Black")

print("Square size", sq1.width, "X", sq1.sides, sq1.color,",",sq2.width,"X",sq2.sides,sq2.color)