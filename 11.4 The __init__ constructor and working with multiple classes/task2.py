import random
import time

class Coordinates:

    count = 0
    def __init__(self,x,y):
        self.x = x
        self.y=y
        Coordinates.count +=1

    def info_point(self):
        print(time.asctime())
        print(f"координата х-{self.x}, координата у-{self.y}, счётчик точек-{self.count}")

while True:
    point_1 = Coordinates(random.randint(0,100),random.randint(0,100))
    point_1.info_point()
    if point_1.count >100:
        break