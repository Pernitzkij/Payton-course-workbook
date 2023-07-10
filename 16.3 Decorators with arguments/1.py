import functools
from _collections_abc import Callable
from typing import Optional

def pred_dec(_fanc=None,*,duble=1):
    def do_twice_dec(fanc:Callable)->Optional:
        @functools.wraps(fanc)
        def wraps(*args,**kwargs)->Optional:
            for _ in range(duble):
                print('Функция повтора запущена ')
                fanc(*args, **kwargs)
            print('Функция отработала')
        return wraps

    if _fanc is None:
        return do_twice_dec
    else:
        return do_twice_dec(_fanc)


@pred_dec(duble=2)
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))

greeting("hello")




