import time
from math import factorial as fact


def time_out(fanky):
    time_input = time.perf_counter()
    fanky()
    time.sleep(0)
    time_sec = (time.perf_counter() - time_input) * 10 ** 3
    print(time_sec)
    return ("The time of execution of above program is :",
            (time_sec), "ms")


def fanky():
    i = 1
    sgn = -1
    a = 13591409
    b = 545140134
    c = 640320
    d = c ** (3 / 2)
    s = a / d
    ss = 3
    while str(ss)[:12] != '3.1415926535':
        tmp = (sgn * fact(6 * i) * (a + b * i) /
               (fact(3 * i) * fact(i) ** 3 * d * c ** (3 * i)))
        s += tmp
        sgn *= -1
        i += 1
        ss = 1 / (12 * s)

    return ss


def gen():
    class Aountor:
        def __init__(self, count):
            self.count = count

        def easy_numer(self):
            for i_num in range(1, self.count):
                self.k = 0
                for i in range(2, i_num // 2 + 1):

                    if i_num % i == 0:
                        self.k = self.k + 1
                if self.k <= 0 and i_num != 1:
                    yield i_num

    while True:
        my_iter = Aountor(int(input('Кол-во элементов: ')))
        for i in my_iter.easy_numer():
            yield i


print(time_out(fanky))
print(time_out(gen))
