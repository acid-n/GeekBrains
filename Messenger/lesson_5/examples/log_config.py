"""
Простейшее логгирование
"""

import logging

# Создаем объект-логгер с именем app.main
LOG = logging.getLogger('app.main')

# Создаем объект форматирования
FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")

# Создаем файловый обработчик логгирования (можно задать кодировку)
FILE_HANDLER = logging.FileHandler("app.main.log", encoding='utf-8')
# fh.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(FORMATTER)

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логгирования
LOG.addHandler(FILE_HANDLER)
LOG.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # Создаем потоковый обработчик логгирования (по умолчанию sys.stderr)
    STREAM_HANDLER = logging.StreamHandler()
    # console.setLevel(logging.DEBUG)
    STREAM_HANDLER.setFormatter(FORMATTER)
    LOG.addHandler(STREAM_HANDLER)
    # В логгирование передаем имя текущей функции и имя вызываемой функции
    LOG.debug('Отладочное сообщение')