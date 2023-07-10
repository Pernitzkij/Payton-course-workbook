import datetime


def logged(func):
    def wrapped(*args, **kwargs):
        print("Запуск функции произошёл в:", datetime.datetime.now())
        return func(*args, **kwargs)

    return wrapped


def decorator(cls):
    for i_method in dir(cls):
        if not i_method.startswith('__'):

            a = getattr(cls, i_method)

            decorated_a = logged(a)
            setattr(cls, i_method, decorated_a)
    return cls


@decorator
class A:

    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


A().test_sum_1()
A().test_sum_1()