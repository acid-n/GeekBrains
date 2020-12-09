"""
Журналирование (логгирование) с использованием модуля logging.
Расширенная настройка. Форматирование, обработчики.
"""

import logging

# Создать логгер - регистратор верхнего уровня с именем app.main
LOG = logging.getLogger('app.main')

# Создать обработчик
FILE_HANDLER = logging.FileHandler("app.log", encoding='utf-8')
# Выводим сообщения с уровнем DEBUG
FILE_HANDLER.setLevel(logging.DEBUG)

# Создать объект Formatter
# Определить формат сообщений
FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")

# Подключить объект Formatter к обработчику
FILE_HANDLER.setFormatter(FORMATTER)

# Добавить обработчик к регистратору
LOG.addHandler(FILE_HANDLER)
LOG.setLevel(logging.DEBUG)

# Передать сообщение обработчику
LOG.info('Информационное сообщение')