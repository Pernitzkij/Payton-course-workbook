class Resors:
    def __init__(self, *args):
        pass
    def open(self, *args):
        pass



class Example:
    def __init__(self, *args):
        # self.args=args
        # self.resors=None
        print("Вызов __init__")

    def __enter__(self):
        # self.resors=Resors()
        # self.resors.open(*self.args)
        print('Вызов __enter__')
        return True

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Вызов __exit__')

        return True





my_obj = Example()

with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')

    with my_obj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')
    with my_obj as obj5:
        print('Новый код')
        with my_obj as obj35:
            print('Новый код продолжение')

    print('Я обязательно выведусь...')