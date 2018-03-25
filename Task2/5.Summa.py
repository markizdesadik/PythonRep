#!/usr/bin/python
# -*- coding: utf-8 -*-
# Labotskiy Vasiliy

"""
Задание 5: Псевдосумма.

УСЛОВИЕ:
Принимать любое натуральное число. (по условию задачи для приема числа
Выдавать сумму цифр, из которых число состоит.
Не использовать оператор "+" и встроенную функцию sum().

Пример:
456 >> 15
"""

this_number = 456

base = [i for i in list(str(this_number))]
our_sum = 0
for i in base:
    our_sum -= int(i)

print(abs(our_sum))
