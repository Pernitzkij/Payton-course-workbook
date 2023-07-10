# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость,
# и каждый умеет двигаться и подавать сигнал. В парке транспорта стоят:
#
# Автомобили. Они могут ездить только по земле.
# Лодки. Ездят только по воде.
# Амфибии. Могут перемещаться и по земле, и по воде.
# Напишите код, который реализует соответствующие классы и методы.
# Класс «Транспорт» должен быть абстрактным и содержать абстрактные методы.
#
# Также добавьте класс-примесь, в котором реализован функционал проигрывания музыки.
# «Замешайте» этот класс в «Амфибию»


from abc import ABC, abstractmethod


class Transpore(ABC):
    def __init__(self, color: str, speed: int):
        self.color = color
        self.speed = speed

    @abstractmethod
    def move(self):
        pass

    def signal(self):
        print(f"{__class__.__name__} подаёт сигнал")


class Auto(Transpore):
    def __init__(self, color: str, speed: int):
        super().__init__(color, speed)
        self.name = Auto.__name__

    def move(self):
        print(f"{Auto.__class__.__name__} двигается со скоростью {self.speed} ", end='')
        print('по земле')


class Music:
    def signal(self):
        print(f"{Amphibian.__class__.__name__} проигрывает музыку")


class Amphibian(Music, Transpore):
    def __init__(self, color: str, speed: int):
        super().__init__(color, speed)

    def move(self):
        print(f"{Amphibian.__class__.__name__} двигается со скоростью {self.speed} ", end='')
        print('по воде')


BMW = Auto(color="blak", speed=200)
BMW.move()
BMW.signal()

lor = Amphibian(color="blak", speed=200)
lor.move()
lor.signal()
