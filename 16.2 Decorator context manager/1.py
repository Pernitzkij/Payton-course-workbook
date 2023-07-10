import time
from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def timer() -> Iterator:
    start = time.time()
    time.sleep(0.3)
    try:
        yield
    except Exception as ex:
        print('Сработало исключение', ex)
    else:
        print('Программа прошла без ошибок')
    finally:
        print('Время работы программы-', time.time() - start)


with timer():
    print('Первая часть')
    desk = list(map(int, range(500)))

with timer():
    print('Вторая часть часть')
    desk1 = list(map(int, range(54000)))
