#!/usr/bin/python
# -*- coding: utf-8 -*-
# Labotskiy Vasiliy

"""Задание 1: Частота буквы.

УСЛОВИЕ:
Посчитать процентное соотношение букв в тексте. Заглавные и строчные приравниваются.
Вывести словарь: ключ - буква, значение - процент (до десятых), в котором эта буква встречается в тексте.

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.

Пример:
"ABCda" >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}
"""


def percentage(text):
    abw = 'qwertyuiopasdfghjklzxcvbnm'
    List1 = [f for f in this_text.lower() if f in abw]
    List1.sort()
    List = {}
    for f in List1:
        if f in List:
            List[f] += f
        else:
            List[f] = f
    for f in List:
        List[f] = round((len(List[f]) / len(List1) * 100), 1)
    return List


# this_text = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. ' \
#             'Donec rutrum congue leo eget malesuada.'
this_text = "asbcda"
print(percentage(this_text))
