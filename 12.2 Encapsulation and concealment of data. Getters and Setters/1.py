class Point:

    def __init__(self, x, y):
        self.__x = 0
        self.__y = 0
        self.set_point(x, y)

    def get_point(self):
        return self.__x, self.__y

    def set_point(self, x, y):
        if self.verifex(x):
            self.__x = x
        if self.verifex(y):
            self.__y = y

    def verifex(self, arg):
        if isinstance(arg, int):
            return arg
        else:
            raise ValueError("Не верный тип данных", arg)

    def __str__(self):
        return self.__x, self.__y


point = Point(66, 4)

print(point.get_point())

point.set_point(3, 5)
print(point.get_point())
