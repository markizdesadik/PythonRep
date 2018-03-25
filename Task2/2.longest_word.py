#!/usr/bin/python
# -*- coding: utf-8 -*-
# Labotskiy Vasiliy

"""
Задание 2: Самое длинное слово.

УСЛОВИЕ:
Найти слово максимальной длины в тексте.
Вывести это слово. Если таких слов несколько - вывести все.

Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus.
Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.
"""

this_text = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. ' \
            'Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.'

words = [word.rstrip('.') for word in this_text.split()]
print([word for word in words if len(word) == max(len(word) for word in words)])
