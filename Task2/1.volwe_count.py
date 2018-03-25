#!/usr/bin/python
# -*- coding: utf-8 -*-
# Labotskiy Vasiliy

"""
Задание 1: И снова гласные.

УСЛОВИЕ:
Посчитать количество гласных в каждом слове текста.
Вывести максимальное количество гласных в одном слове.

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus.
Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.

Гласные: A, E, I, O, U, Y
"""

this_text = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. ' \
            'Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.'

list_of_vowels = 'AEIOUY'

words = this_text.split()
volwe_in_word_count = []
for word in words:
    count = 0
    for volwe in word:
        if volwe.upper() in list_of_vowels:
            count += 1
    volwe_in_word_count.append(count)
print(max(volwe_in_word_count))
