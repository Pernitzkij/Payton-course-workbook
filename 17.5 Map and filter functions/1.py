"""Сортировка в одну строку"""

numbers = input("Введите числа: ")
print(sorted(list(map(int, numbers.split()))))