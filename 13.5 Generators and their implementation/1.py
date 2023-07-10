class Aountor:
    def __init__(self, count):
        self.count = count

    def easy_numer(self):
        for i_num in range(1,self.count):
            self.k = 0
            for i in range(2, i_num // 2 + 1):

                if i_num % i == 0:
                    self.k = self.k + 1
            if self.k <= 0 and i_num != 1:
                yield i_num


while True:
    my_iter = Aountor(int(input('Кол-во элементов: ')))
    for i in my_iter.easy_numer():
        print(i)


