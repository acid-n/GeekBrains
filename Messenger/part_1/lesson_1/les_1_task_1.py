"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции

ВНИМАНИЕ!!: сдача задания - папка Lesson_1_Ivanov.zip - в ней файлы исходного кода - дальше архив
и его прикладываем к форме сдачи.
Все другие варианты получают оценку НЕ СДАНО!!! - имена файлов task_1 - task_5
"""

words = [
    'разработка',
    'сокет',
    'декоратор'
]

unicode_words = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
]

for w in words:
    print(f'Слово: {w}, тип: {type(w)}')

for u in unicode_words:
    print(f'Набор кодовых точек: {u}, тип: {type(u)}')
