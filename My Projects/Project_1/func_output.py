from typing import Optional
import itertools

"""Модуль для вывода данных"""

def prefix(age_prefix) -> Optional:
    if 11 <= age_prefix % 100 <= 19:
        prefix = 'лет'
    elif age_prefix % 10 == 1:
        prefix = 'год'
    elif 2 <= age_prefix % 10 <= 4:
        prefix = 'года'
    else:
        prefix = 'лет'
    return prefix


def func_print(log, data, step) -> Optional:

    for i in log:
        if 'Возраст' in i:
            age = str(i).split('Возраст:')
            age = int(age[1])

            print(f'Возраст:{age} {prefix(age)}')

        elif 'ОГРНИП' in i or 'ИНН' in i or 'Расчётный счёт' in i \
                or 'Название банка' in i or 'БИК' in i or 'Корреспондентский счёт' in i:
            if step == 7:
                continue
            else:
                print(i)
        else:
            print(i)

    for i in data:
        for key, value in itertools.islice(i.items(), step):

            if key == 'Возраст':
                age = int(value)
                print(f'Возраст:{age} {prefix(age)}')

            else:
                print(key, ':', value)
        print()

def general_info(log, data):
    try:

        while True:
            print('-' * 32)
            print('ГЛАВНОЕ МЕНЮ\n1 - Личная информация\n2 - Вся информация\n0 - Назад')
            option = int(input('Введите номер пункта меню: '))
            if option == 0:
                return

            if option == 1:
                completeness = 7
                func_print(log, data, completeness)
            if option == 2:
                completeness = 13
                func_print(log, data, completeness)


    except ValueError as f:

        print('Сработала ошибка ввода', f, 'Вы вернулись в главное меню')

