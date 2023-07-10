#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Сountor:
    def __init__(self, start=1):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        start = self.start
        self.start += 1
        if start == 100:
            raise ValueError('Куда так много')
        return start


my_iter = Сountor()

for i_elem in my_iter:
    if my_iter == 100:
        break
    print(i_elem)
