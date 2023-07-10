class Human:

    def __init__(self, name="НЕТ", age=1):

        self.__count = 0
        self.set_age(age)
        self.set_name(name)

    def verificantion_age(self, arg):
        self.__set_count()
        if isinstance(arg, int):
            if arg > 0 and arg < 100:
                return arg
            else:
                raise ImportError("Возраст не допустим")
        else:
            raise ValueError('Это не возраст')

    def verificantion_name(self, name):
        self.__set_count()
        if isinstance(name, str):
            if name.isalpha():
                return name
            else:
                raise ImportError('Не имя')
        else:
            raise ValueError('Не строка')

    def __str__(self):
        return self.__name, self.__age

    def get_name(self):
        return 'Имя', self.__name

    def set_name(self, name):
        if self.verificantion_name(name):
            self.__name = name

    def get_age(self):
        return 'Возраст', self.__age

    def set_age(self, age):
        if self.verificantion_age(age):
            self.__age = age

    def get_count(self):
        return 'Количество итераций', self.__count

    def __set_count(self):
        self.__count += 1


humen = Human()
print(*humen.get_count())
print(*humen.get_name())
print(*humen.get_age())
print()
humen.set_age(99)
humen.set_name('Ма5кс')

print(*humen.get_count())
print(*humen.get_name())
print(*humen.get_age())
print()
humen.set_age(55555)
humen.set_name('Мкс')
print(*humen.get_count())
print(*humen.get_name())
print(*humen.get_age())
