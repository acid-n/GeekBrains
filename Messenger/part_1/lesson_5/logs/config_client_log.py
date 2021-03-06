"""
Конфиг клиентского логгера
"""

import sys
import os
import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler

sys.path.append('../')
from common.variables import LOGGING_LEVEL

# Настраиваем формат логов
CLIENT_FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(message)s')

# Заносим в найстройки имя файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'client.log')

# Создаем поток вывода логов
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(CLIENT_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)

LOG_FILE = TimedRotatingFileHandler(PATH, encoding='utf-8', interval=1, when='midnight')
LOG_FILE.setFormatter(CLIENT_FORMATTER)

# Создаем регистратор и настраиваем его
LOGGER = logging.getLogger('client')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)

# Отладка
if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')