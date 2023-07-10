from typing import Optional
import itertools
import re

"""Модуль для ввода данных"""


def input_dict() -> Optional:
    client: dict = {'Имя': None, 'Возраст': None, 'Телефон': None,
                    'Электронная почта': None, 'Индекс': None,
                    'Почтовый адрес': None, 'Дополнительная информация': None,
                    'ОГРНИП': None, 'ИНН': None, 'Расчётный счёт': None,
                    'Название банка': None, 'БИК': None, 'Корреспондентский счёт': None}
    try:

        while True:
            print('-' * 32)
            print('ГЛАВНОЕ МЕНЮ\n1 - Личная информация\n2 - Информация о предпринимателе\n0 - Назад')

            option = int(input('Введите номер пункта меню: '))
            if option == 0:
                return client

            if option == 1:
                for key in itertools.islice(client.keys(), 7):
                    if key == 'Возраст':
                        while True:
                            age = int(input(f'{key}: Введите значение '))
                            if age > 0:
                                break
                            print('Возраст должен быть положительным')
                        client[key] = age
                    elif key == 'Телефон':
                        while True:
                            phone_number = (input(f'{key}: Введите значение в формате (+7ХХХХХХХХХХ) '))
                            rule = re.compile(r'^((\+7|7|8)+([0-9]){10})$')
                            if not rule.search(phone_number):
                                print('Номер не корректен')
                            else:
                                break
                        client[key] = phone_number

                    elif key == 'Электронная почта':
                        while True:
                            email = (input(f'{key}: Введите значение '))
                            rule = re.compile(r"^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$")
                            if not rule.search(email):
                                print('Адрес почты не корректен')
                            else:
                                break
                        client[key] = email

                    elif key == 'Индекс':
                        while True:
                            index = (input(f'{key}: Введите значение '))
                            rule = re.compile(r"\d{6}")
                            if not rule.search(index):
                                print('Индекс не корректен')
                            else:
                                break
                        client[key] = index

                    else:
                        client[key] = input(f'{key}: Введите значение ')

            if option == 2:
                for key in itertools.islice(client.keys(), 7, 13):
                    if key == 'ОГРНИП':
                        while True:
                            numer_ogrip = (input(f'{key}: Введите значение '))
                            rule = re.compile(r"\d{15}")
                            if not rule.search(numer_ogrip):
                                print('ОГРНИП не корректен')
                            else:
                                break
                        client[key] = numer_ogrip
                    elif key == 'ИНН':
                        while True:
                            numer_inn = (input(f'{key}: Введите значение '))
                            rule = re.compile(r"\d{10}")
                            if not rule.search(numer_inn):
                                print('ИНН не корректен')
                            else:
                                break
                        client[key] = numer_inn

                    elif key == 'Расчётный счёт':
                        while True:
                            numer_bank = (input(f'{key}: Введите значение '))
                            rule = re.compile(r"\d{20}")
                            if not rule.search(numer_bank):
                                print('Расчётный счёт не корректен')
                            else:
                                break
                        client[key] = numer_bank

                    else:
                        client[key] = input(f'{key}: Введите значение ')

                print(client)

    except ValueError as f:
        print('Сработала ошибка ввода', f, 'Введенные данные сохранены')

    finally:
        return client
