class Robots:
    def __init__(self, model, work):
        self.model = model
        self.work = work

    def operator(self):
        print('Робот', self.model, 'выполняет команду:', self.work)


class Robo_duster(Robots):
    def __init__(self, model, work):
        super().__init__(model, work)
        self.bag = 0

    def operator(self):
        super().operator()
        self.bag += 1
        print('Размер бака:', self.bag)


class War_robo(Robots):
    def __init__(self, mobel, work, arm):
        super().__init__(mobel, work)
        self.arm = arm

    def operator(self):
        super().operator()
        print('Используется оружие', self.arm)


class Woter_robo(War_robo):
    def __init__(self, mobel, work, arm):
        super().__init__(mobel, work, arm)
        self.depth = -10

    def operator(self):
        super().operator()

        print('Глубина:', self.depth, '\n')
        self.depth -= 10


# duster=Robo_duster('R2B2','пылесосит')
#
# duster.operator()
# duster.operator()

# war_robo= War_robo       ('R1t3','Защита',"бластер")
# war_robo.operator()

woter_robo = Woter_robo('w4a4', 'Патруль', 'гарпун')
woter_robo.operator()
woter_robo.work = 'Атака подводнй цели'
woter_robo.operator()
woter_robo.work = 'Обследует периметр'
woter_robo.operator()
woter_robo.work = 'Обследует дно'
woter_robo.operator()
