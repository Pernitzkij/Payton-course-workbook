class Can_Fly:
    def __init__(self,height=0,spead=0):
        self.height=height
        self.spead=spead


    def take_off(self):
        pass

    def take_on(self):
        pass


    def fly(self):
        pass

    def __str__(self):
        return 'Высота_',self.height,'\nСкорость-',self.spead



class BaterFly(Can_Fly):
    def take_off(self):
        self.height+=1


    def fly(self):
        self.spead = 0.5

class Rocket(Can_Fly):
    def take_off(self):
        self.height+=500
        self.spead=1000
    def take_on(self):
        if self.height <=0:
            pass
        else:
            self.height-=500

    def big_ban(self):
        if self.height<=0:
            print('BANG')
            self.spead=0

bater=BaterFly()
for _ in range(5):
    bater.fly()
    bater.take_off()
print(*bater.__str__())

roket=Rocket()
for _ in range(5):
    roket.take_off()
    print(*roket.__str__())

for _ in range(5):

    roket.take_on()
    print(*roket.__str__())
    roket.big_ban()
print(*roket.__str__())