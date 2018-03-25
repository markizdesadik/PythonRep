#!/usr/bin/python
# -*- coding: utf-8 -*-
# Labotskiy Vasiliy

"""
Задание 3: Реверс'em!

УСЛОВИЕ:
Изменить в тексте порядок следования:
- букв в словах;
- слов в предложениях;
- предложений в тексте.
Вывести модифицированный текст.

Текст:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada.
Cras ultricies ligula sed magna dictum porta.
"""

this_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. ' \
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. ' \
            'Cras ultricies ligula sed magna dictum porta.'


def revers_letter(text):
    """Returns a string with the order of letters in words changed in the text

    """
    line_of_text = []
    for words in text.split('.'):
        line_of_text.append('.')
        for word in words.split():
            line_of_text.append(word[::-1])
    return ' '.join(line_of_text[1::])


def revers_word(text):
    """Returns a string with the word order in the sentences changed in the text

    """
    line_of_text = ''
    for words in text.split('.'):
        line_of_text += '. '
        temp = [word for word in words.split()]
        temp.reverse()
        line_of_text += ' '.join(temp)
    return line_of_text.strip('.')


def revers_sentence(text):
    """Returns a string with the order of sentences in the text changed in the text

    """
    sentence = [sent.rstrip('.') for sent in text.split('.')]
    sentence.reverse()
    return '.'.join(sentence)


print(revers_letter(this_text))
print(revers_sentence(revers_word(revers_letter(this_text))))
