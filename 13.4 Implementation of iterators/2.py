import random

"""Задача 2. Случайная сумма
Алексею по работе необходимо обрабатывать огромные массивы данных из миллионов элементов.
 Каждый новый элемент — это сумма случайного вещественного числа от 0 до 1 и предыдущего элемента
  (первый элемент — просто случайное вещественное число от 0 до 1). 
  Алексею нельзя хранить в памяти весь этот список, а со значениями работать как-то надо.

Помогите Алексею, реализуйте такой класс-итератор и проверьте его работу. 
Также сделайте, чтобы при каждом новом вызове итератора в цикле значения считались заново.

"""


class Aountor:
    def __init__(self, count):
        self.caunt_iter = 0
        self.count = count
        self.start = random.uniform(0, 1)

    def __iter__(self):
        return self

    def __next__(self):

        if self.caunt_iter < self.count:

            self.start += random.uniform(0, 1)
            self.caunt_iter += 1
            return self.start
        else:
            raise StopIteration('Список пуст')


while True:
    my_iter = Aountor(int(input('Кол-во элементов: ')))
    print("Элементы итератора: ")

    for i_elem in my_iter:
        print(round(i_elem, 2))
