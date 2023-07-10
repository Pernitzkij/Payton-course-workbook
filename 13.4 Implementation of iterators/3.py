class Aountor:
    def __init__(self, count):
        self.caunt_iter = 0
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):

        if self.caunt_iter < self.count:

            self.caunt_iter += 1
            return self.caunt_iter
        else:
            raise StopIteration('Список пуст')


while True:
    my_iter = Aountor(int(input('Кол-во элементов: ')))
    print("Элементы итератора: ")

    for i_elem in my_iter:
        k = 0
        for i in range(2, i_elem // 2 + 1):

            if i_elem % i == 0:
                k = k + 1
        if k <= 0 and i_elem != 1:
            print(i_elem)
