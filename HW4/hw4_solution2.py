#!/usr/bin/python
# -*- coding: utf-8 -*-
# Labotskiy Vasiliy

"""
Задание 2: Послесловие...

УСЛОВИЕ:
Дан текст и ограничение длины текста (в количестве символов). Необходимо, в случае, если текст не помещается в
ограничение обрезать его, но при этом слова не должны обрываться на середине, если граница обрезки приходится на слово,
начинающееся на гласную - оставляем слово целиком, если на согласную - убираем слово целиком.


Текст:
Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.

Пример:
text = "Proin eget tortor risus."

limit = 24
output = "Proin eget tortor risus."

limit = 22
output = "Proin eget tortor"

limit = 13
output = "Proin eget"

limit = 8
output = "Proin eget"
"""

text = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.'

limit = 36


def ellipsis(text, limit=len(text)):
    abw = 'aeuioAEUIO'
    len_word = 0
    counter = 0
    sub_list = []
    if len(text) == limit:
        return text
    for word in text.split():
        counter += 1
        len_word += len(word)
        sub_list.append(word)
        if len_word >= limit - counter:
            if word[0] in abw:
                return " ".join(sub_list)
            else:
                sub_list.pop()
                return " ".join(sub_list)


print(text[:limit + 1])
print(ellipsis(text))
