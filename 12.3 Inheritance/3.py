class DivisionError(Exception):
    def __init__(self):
        self.message = 'нельзя делить большее на меньшее'

    def __str__(self):
        return f'{self.message}'


result = []

with open('numbers.txt', 'r', encoding='utf-8') as file_read:
    for line in file_read:
        result = line.split()
        print(result)
        try:
            if int(result[0]) > int(result[1]):
                print('Результат деления:', int(result[0]) / int(result[1]))
            else:
                raise DivisionError

        except DivisionError:
            # raise 
            print('нельзя делить большее на меньшее') 