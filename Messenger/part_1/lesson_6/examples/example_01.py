"""
Простейший декоратор-функция
"""

import time


def decorator(func):
    # Сам декоратор
    def wrapper():
        # Обертка
        print(f'Сейчас выполняется функция-обертка')
        time.sleep(2)
        print(f'Это просто ссылка на экземпляр оборачиваемой функции {func}')
        time.sleep(2)
        print(f'Выполняем оборачиваемую (исходную) функцию...')
        time.sleep(2)
        func()
        time.sleep(2)
        print(f'Выходим из обертки')
        # обертка может ничего не возвращать

    return wrapper


@decorator
def some_text():
    # Какая-то логика
    print(f'Вычисления')


some_text()
