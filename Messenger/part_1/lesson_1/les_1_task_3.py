"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

import string


def check(value):
    for letter in value:
        if letter not in string.ascii_letters:
            return False
    return True


words = [
    'attribute',
    'класс',
    'функция',
    'type'
]

for word in words:
    if not check(word):
        print(f'Слово "{word}" невозможно записать в байтовом типе с помощью маркировки b')
