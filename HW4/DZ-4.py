# -*- coding: utf8 -*-

""" Это файл тестов. Они все должны проходить без ошибок. """

import hw4_solution1
import hw4_solution2


def tests_for_hw4_solution1():
    """Тесты задачи 1"""

    assert hw4_solution1.percentage("A") == {'a': 100.0}
    assert hw4_solution1.percentage("ABCda") == {
        'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0
    }
    assert hw4_solution1.percentage("AsBCda") == {
        'a': 33.3, 'b': 16.7, 'c': 16.7, 'd': 16.7, 's': 16.7
    }
    assert hw4_solution1.percentage("q TyU#!{}.") == {
        'q': 25.0, 't': 25.0, 'y': 25.0, 'u': 25.0
    }
    assert sum(hw4_solution1.percentage("q TyU#!{}.").values()) == 100.0

    assert hw4_solution1.percentage("A") == {'a': 100.0}
    assert hw4_solution1.percentage("ABCda") == {
        'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0
    }
    assert hw4_solution1.percentage("AsBCda") == {
        'a': 33.3, 'b': 16.7, 'c': 16.7, 'd': 16.7, 's': 16.7
    }
    assert hw4_solution1.percentage("q TyU#!{}.") == {
        'q': 25.0, 't': 25.0, 'y': 25.0, 'u': 25.0
    }
    assert sum(hw4_solution1.percentage_2("q TyU#!{}.").values()) == 100.0


def tests_for_hw4_solution2():
    """Тесты задачи 2"""

    text = "Proin eget tortor risus."
    assert hw4_solution2.ellipsis(text) == "Proin eget tortor risus."
    assert hw4_solution2.ellipsis(text, 24) == "Proin eget tortor risus."
    assert hw4_solution2.ellipsis(text, 22) == "Proin eget tortor"
    assert hw4_solution2.ellipsis(text, 13) == "Proin eget"
    assert hw4_solution2.ellipsis(text, 8) == "Proin eget"

if __name__ == "__main__":

    tests_for_hw4_solution1()
    tests_for_hw4_solution2()