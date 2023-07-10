from typing import Callable, Any


def do_twice(func: Callable) -> Callable:
    """декоратор do_twice, который дважды вызывает декорируемую функцию"""

    def wrapped_func(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapped_func


@do_twice
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting("3343")