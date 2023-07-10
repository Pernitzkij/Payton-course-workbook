class Tayota:
    # color = 'red'
    # speed_max = 200
    # speed_earn = 0
    def __init__(self, color, speed_max, speed_earn):
        self.color = color
        self.speed_max = speed_max
        self.speed_earn = speed_earn

    def info(self):
        print(f"Цвет-{self.color}, скорость-{self.speed_max}, скорость текущая-{self.speed_earn}")


cars = Tayota('чёрный', 200, 7)

cars.info()
