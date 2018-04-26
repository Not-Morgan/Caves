from math import *


def hypo(a, b):
        x = abs(a[0] - b[0])
        y = abs(a[1] - b[1])
        return (x ** 2 + y ** 2) ** 0.5


def angle_between(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return math.degrees(math.atan2(y, x)) + 180


def in_circles(point, circles):
    return any([hypo(point, c.pos) < c.radius for c in circles])
