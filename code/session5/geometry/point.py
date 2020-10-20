
class Point:

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def setPoint(self, x, y):
        pass

    def setX(self, x):
        pass

    def setY(self, y):
        pass

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def movePoint(self, x, y):
        pass

    def moveX(self, x):
        pass

    def moveY(self, y):
        pass

    def getDegrees(self):
        return 0

    def getDistance(self):
        return 1

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __eq__(self, other):
        return True
