#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def func(a, b, type=0):
    def func2():
        if type == 0:
            res = a * b / 2
            res = f'Для значений {a}, {b} площадь треугольника = {res}'
            return res
        elif type == 1:
            res = a * b
            res = f'Для значений {a}, {b} площадь прямоугольника = {res}'
            return res
    return func2



if __name__ == '__main__':
    print(func(5, 3)())
    print(func(8, 10, 1)())
    print(func(3, 5, 0)())
    print(func(2, 2, 1)())
