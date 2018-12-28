import math
import random

class Circle:
    def __init__(self):
        self.radius = random.uniform(1.1, 9.5)
    def calCircumference(self):
        return math.pi * 2 * self.radius
    def calDiameter(self):
        return 2* self.radius
    def calArea(self):
        return math.pi * (self.radius ** 2)

circles = []
for i in range(0,10):
    c = Circle()
    #c.radius = random.uniform(1.1,9.5)
    circles.append(c)


for c in circles:
    print("Diameter : ", round(c.calDiameter(),2), "\tcircumference : ", round(c.calCircumference(),2),\
          "\tArea :",round(c.calArea(),2))