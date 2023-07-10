from time import sleep
import functools
from _collections_abc import Callable
from typing import Optional, Any


def slow_it_now(_func=None, *, n=1) -> Callable:
    def slowdown_ns(func) -> Optional:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            sleep(n)
            func(*args, **kwargs)
            return f'Время простоя-{n} секунд'

        return wrapper

    if _func is None:
        return slowdown_ns
    else:
        return slowdown_ns(_func)


@slow_it_now(n=3)
def test() -> None:
    """
    Проверка декоратора и вывод простого сообщения

    :return:
    """
    print('<Тут что-то происходит...>')


print(test())
