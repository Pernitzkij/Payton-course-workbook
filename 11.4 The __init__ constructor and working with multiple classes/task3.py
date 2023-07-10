class Potato:
    """класс картошка, параметры зрелость и количество. по умолчанию зрелость 0"""
    maturity = 0


    def maturity_fun(self):

        if self.maturity == 0:
            print('Картошка ещё не посажена!')
        if self.maturity == 1:
            print('Картошка посажена!')
        if self.maturity == 2:
            print('Картошка растёт!')
        if self.maturity == 3:
            print('Картошка вырасла!')
class Potato_clumba:
    """класс грядка картошки, растит картошку и показывает информацию о картошке"""
    def __init__(self,count_potato):
        self.count_potato = count_potato
    def maturity_clumba(self):
        Potato.maturity +=1
        if Potato.maturity !=4:
            print('Картошка прорастает!')
            print(f'Всего картошки {self.count_potato}')
            for i in range(1,self.count_potato+1):
                if Potato.maturity !=3 :
                    print(f'Картошка {i}','посажена' if Potato.maturity==1  else 'Зелёная'  )
                else:
                    print(f'Картошка {i}', 'Зрелая')
        else:
            print('Вся картошка созрела. Можно собирать!')

pop = Potato()
pop_clum = Potato_clumba(3)
while True:
    pop.maturity_fun()
    pop_clum.maturity_clumba()
    if Potato.maturity ==4:
        break