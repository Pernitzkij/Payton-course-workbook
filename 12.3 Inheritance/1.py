class Spips:
    def __init__(self, model):
        self.model = model


class WarShip(Spips):
    def __init__(self, model, arm):
        super().__init__(model)
        self.arm = arm

    def atak(self):
        print(self.model, 'атакует с помощью оружия', self.arm)


class CargoShip(Spips):
    def __init__(self, model):
        super().__init__(model)
        self.lou_toner = 0

    def info(self):
        print(self.model, 'загружен на:', self.lou_toner)

    def up_toner(self):
        self.lou_toner += 1

    def doun_toner(self):
        self.lou_toner -= 1


war = WarShip('Атмо', 'ракеты')
war.atak()

cargo = CargoShip('Патриот')
cargo.info()
cargo.up_toner()
cargo.info()
cargo.up_toner()
cargo.info()
