# Простейший декоратор-функция

import time
import requests


def decorator(func):
    # Сам декоратор
    def wrapper(*args, **kwargs):
        # Обертка
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения исходной функции : {round(end - start, 2)} секунд')

    return wrapper


@decorator
def get_wp(url):
    # Получаем ответ сервера
    # 200 - запрос успешно обработан
    print(f'Выполняем расчет')
    res = requests.get(url)
    print(f'Проверка адреса {url} - ответ {res}')
    return res


urls = ('https://mail.ru', 'https://yandex.ru', 'https://google.ru', 'https://vk.com', 'https://ru.wikipedia.org')

for url in urls:
    get_wp(url)
