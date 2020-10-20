class Rectangle:
    def __init__(self, length = 1, width = 1):
        self.__length = length
        self.__width = width

    def setLength(self, length):
        self.__length = length

    def setWidth(self, width):
        self.__width = width

    def getLength(self):
        return self.__length

    def getWidth(self):
        return self.__width

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

