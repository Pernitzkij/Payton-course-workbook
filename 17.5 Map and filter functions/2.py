"""Сортировка в одну строку"""

print(list(filter(lambda x: not x.isupper() or x.isdigit(),input('Введите последовательность: '))))