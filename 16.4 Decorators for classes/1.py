import functools
from datetime import datetime
import time

def creativ(cls):
    @functools.wraps(cls)
    def wrapper(*args,**kwargs):
        isin=cls(*args,**kwargs)
        print('Время создания инстанса класса',datetime.utcnow())
        print('Директории функции:',end=' ')
        for i in dir(cls):
            if not i.startswith('__'):
                print(i,end=' ')
        
        print( '\nВызвана функция: ', wrapper.__name__)
        return isin
    return wrapper





@creativ
class Calcs:
    def __init__(self,pop=0):
        self.pop=pop

    def one (self):
        print(2*2)

    def two (self):
        print(2*2)


Calcs()
