import math

def circumferemnce(radius):
    return math.pi * 2 * radius

circles = [["First Circle", 4.4,0],["Second Circle", 3.7,0]]
circles[0][2] = circumferemnce(circles[0][1])
print(circles[0][2],circles[0][0])

circles[1][2] = circumferemnce(circles[1][1])
print(circles[1][2],circles[1][0])