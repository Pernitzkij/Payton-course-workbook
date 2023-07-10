import os
from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def in_dir(path) -> Iterator:
    cur_path = None
    if os.path.isdir(path):
        print('Путь является директорией', end=' ---%--- ')
        if os.path.isabs(path):
            print('Путь является абсолютным')

    try:
        cur_path = os.getcwd()
        os.chdir(path)
        yield
    except FileNotFoundError as ex:
        print(ex, 'Такой директории не существует')
    finally:
        os.chdir(cur_path)


with in_dir(os.path.abspath('F:\\')):
    print(os.listdir())
