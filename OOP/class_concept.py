import math

def circumferemnce(radius):
    return math.pi * 2 * radius

class circle:
    pass

circle1 = circle()
circle1.radius = 4.4
print(circle1.radius)
print(circumferemnce(circle1.radius))

circle2 = circle()
circle2.radius = 3.7
print(circle2.radius)
print(circumferemnce(circle2.radius))