# Конфиг серверного логгера

import sys
import os
import logging
from logging.handlers import TimedRotatingFileHandler

sys.path.append('../')
from common.variables import LOGGING_LEVEL

# Настраиваем формат логов
SERVER_FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(message)s')

# Заносим в найстройки имя файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

# Создаем потоки вывода логов
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)

# Настраиваем, что каждый день будет создаваться новый файл с логами
LOG_FILE = TimedRotatingFileHandler(PATH, encoding='utf-8', interval=1, when='midnight')
LOG_FILE.setFormatter(SERVER_FORMATTER)

# Создаем регистратор и настраиваем его
LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)

# Отладка
if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')