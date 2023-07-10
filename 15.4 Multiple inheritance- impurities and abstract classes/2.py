from abc import ABC, abstractmethod


class Shapes(ABC):
    def __init__(self, x=None, y=None, long=None, width=None):
        self.x = x
        self.y = y
        self.long = long
        self.width = width

    @abstractmethod
    def sizes(self, proofreader):
        pass

    @abstractmethod
    def movement(self, new_x, new_y):
        pass

    def __str__(self):
        return 'Координаты X: {} Y: {}\nРазмеры Длинна: {} Ширина: {}'.format(self.x, self.y, self.long, self.width)


class primise:
    def sizes(self, proofreader_l, proofreader_w):
        self.long *= proofreader_l
        self.width *= proofreader_w


class Cube(Shapes):
    def __init__(self, x=None, y=None, long=None):
        super().__init__(x, y, long)

    def sizes(self, proofreader):
        self.long *= proofreader

    def movement(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def __str__(self):
        return 'Координаты X: {} Y: {}\nРазмеры  {} X {}'.format(self.x, self.y, self.long, self.long)


class Rectangle(primise, Shapes):
    def __init__(self, x=None, y=None, long=None, width=None):
        super().__init__(x, y, long, width)

    def movement(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


print(Cube.__name__)
cube = Cube(x=50, y=60, long=40)
print(cube)
cube.sizes(proofreader=5)
cube.movement(50, 37)

print(cube, '\n')

print(Rectangle.__name__)
rectangle = Rectangle(x=5, y=6, long=4, width=5)
print(rectangle)
rectangle.sizes(5, 2)
rectangle.movement(5, 3)

print(rectangle)
