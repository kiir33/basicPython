import math
import random

class Circle:
    def calCircumference(self):
        return math.pi * 2 * self.radius

circles = []
for i in range(0,10):
    c= Circle()
    c.radius = random.uniform(1.1,9.5)
    #c.circumference = c.calCircumference(c.radius)
    circles.append(c)


for c in circles:
    print("Radius : ", c.radius, "circumference : ", c.calCircumference())

c1 = Circle()
c1.radius = 1/math.pi
print(c1.calCircumference())