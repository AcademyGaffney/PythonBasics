import math

class Point:

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def setPoint(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def movePoint(self, x, y):
        self.x += x
        self.y += y

    def moveX(self, x):
        self.x += x

    def moveY(self, y):
        self.y += y

    def getDegrees(self):
        degrees = math.atan2(self.x, self.y) / math.pi * 180
        if degrees < 0:
            return degrees + 360
        return degrees

    def getDistance(self):
        return (self.x ** 2 + self.y ** 2) ** .5

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        xQuot = self.x / other.x
        yQuot = self.y / other.y
        if xQuot < 1:
            xQuot = 1 / xQuotS
        if yQuot < 1:
            yQuot = 1 / yQuot
        return xQuot < 1.000000000001 and yQuot < 1.000000000001

