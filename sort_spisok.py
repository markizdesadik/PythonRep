#!/usr/bin/python
# -*- coding: utf-8 -*-
# Labotskiy Vasiliy


"""
2 задание:
spisok_studentov = ['Kudrov Artyom', 'Belova Svetlana',
                    'Potyomkin Aleksandr', 'Grishel Nastya',
                    'Pobedin Viktor', 'Siluanov Anton',
                    'Antonenko Pavel', 'Kozin Semen']

Напишите программу, которая:
1) запросит у пользователя, как сортировать, по имени или по фамилии, и в зависимости от выбора пользователя:
2а) выведет на экран список студентов отсортированных в алфавитном порядке по фамилии.
(один студент на строку, порядок 'фамилия-имя' не меняется)
ИЛИ
2б) выведет на экран список студентов отсортированных в алфавитном порядке по имени.
(один студент на строку, порядок 'фамилия-имя' не меняется)
"""

import os
import random
from tkinter import *

spisok_studentov = ['Kudrov Artyom', 'Belova Svetlana',
                    'Potyomkin Aleksandr', 'Grishel Nastya',
                    'Pobedin Viktor', 'Siluanov Anton',
                    'Antonenko Pavel', 'Kozin Semen']


def sorted_more(spisok):
    """Механизм для сортировки"""

    n = 1
    while n < len(spisok):
        for i in range(len(spisok) - n):
            if spisok[i] < spisok[i + 1]:
                spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
        n += 1
    return spisok


def sort_name(spis):
    """сортирует список по имени"""

    text.delete(1.0, END)
    sort = [i.split()[1] for i in spis]
    sort = sorted_more(sort)
    for i in sort:
        for t in spis:
            if ' ' + i in t:
                text.insert(1.0, t + '\n')


def sort_last(spis):
    """сортирует список по фамилии"""

    text.delete(1.0, END)
    sort = sorted(spisok_studentov)
    for i in sort:
        text.insert(1.0, i + '\n')


def save(spis):
    """Записывает рандомное имя в файл"""

    with open(os.getcwd() + '/random_name.txt', 'w') as file:
        file.write(random.choice(spis))


def sort_event(event):
    sort_spis = sort_name(spisok_studentov)


def sort_event_last(event):
    sort_spis = sort_last(spisok_studentov)


def Save_Random(event):
    save(spisok_studentov)
    root.destroy()


root = Tk()
text = Text(root)
Button1 = Button(root, text='name')
Button2 = Button(root, text='last name')
ButtonSave = Button(root, text='Save Random and Quit')

Button1.bind('<Button-1>', sort_event)
Button2.bind('<Button-1>', sort_event_last)
ButtonSave.bind('<Button-1>', Save_Random)

Button1.grid(row=2, column=1)
Button2.grid(row=2, column=3)
ButtonSave.grid(row=2, column=2)
text.grid(row=1, column=1, columnspan=3)
root.mainloop()
