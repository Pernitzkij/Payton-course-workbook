import datetime



def dekr(cls):
    for i_method in dir(cls):
        if i_method.startswith('__'):
            continue






@dekr
class A:

    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


A().test_sum_1()