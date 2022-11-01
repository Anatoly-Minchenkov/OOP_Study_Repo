
from random import randrange, choice


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


def random():
    return randrange(1, 1000)


elements = [choice([Ellipse, Rect, Line])(random(), random(), random(), random()) for i in range(217)]

for elem in elements:
    if elem.__class__ == Line:
        elem.ep = (0, 0)
        elem.sp = (0, 0)




