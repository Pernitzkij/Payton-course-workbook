class Units:
    def __init__(self):
        self.__head = 100
        self.damag = 0

    def down_damag(self):
        pass

    def get_head(self):
        return self.__head

    def __str__(self):
        return self.get_head()


class Warrior(Units):
    def __init__(self, damag):
        super().__init__()
        self.damag = damag

    def down_damag(self):
        super().down_damag()
        head = self.get_head()
        head -= self.damag
        return 'здоровье-', head


class Neitral(Units):
    def __init__(self, damag):
        super().__init__()
        self.damag = damag

    def down_damag(self):
        super().down_damag()
        head = self.get_head()
        head -= (self.damag) * 2
        return 'здоровье-', head


warior = Warrior(9)
print(*warior.down_damag())

neitral = Neitral(6)
print(*neitral.down_damag())
