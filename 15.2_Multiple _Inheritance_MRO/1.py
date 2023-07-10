class Robot(object):

    def __init__(self, model, *args, **kwargs):

        self.model = model

    def __str__(self):

        return  'Робот {} {} model {}'.format(Robot,__class__.__name__, self.model)

    def operate(self):

        print('Я - Робот!')




class CanFly(object):

    def __init__(self, *args, **kwargs):
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч

    def take_off(self):
        self.altitude = 100
        self.velocity = 300

    def fly(self):
        self.altitude = 5000

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

    def operate(self):
        Robot.operate(self)
        print('летим')

    def __str__(self):
        res = super().__str__()
        return res + ' {} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity,
        )


class ScoutDrone(CanFly, Robot):

    def __init__(self, model):
        super().__init__(model=model)

    def operate(self):
        super().operate()
        print('Робот ведет разведку с воздуха')


class WarDrone(CanFly, Robot):

    def __init__(self, model, gun):
        super().__init__(model=model)
        self.gun = gun

    def operate(self):
        super().operate()
        print(f'Робот защищает объект при помощи {self.gun}')

class Robo_Bob(WarDrone):
    def __init__(self,model,name,gun='vintovka'):
        super().__init__(model=model,gun=gun)
        self.name=name

    def operate(self):
        print(Robo_Bob.__name__, 'Патрулирует')
        super().operate()


print()
ScoutDrone('a1').operate()
print()
WarDrone('r2-d2', 'intellect').operate()

Robo_Bob(model='ficus',name='Arisha').operate()
