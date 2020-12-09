"""
Журналирование (логгирование) с использованием модуля logging.
Базовая настройка.
"""

import logging

# Быстрая настройка логгирования может быть выполнена так
logging.basicConfig(
    # файл в который добавляются журналируемые сообщения
    filename="app_01.log",
    # формат формирования сообщения
    # %(levelname)s - уровень важности
    # %(asctime)s - дата попадания записи в журнал
    # %(message)s - текст сообщения
    format="%(levelname)s %(asctime)s %(message)s",
    # будут обрабатывать сообщение с уровнем важности, равным казанному или выше
    level=logging.INFO
    # level=logging.DEBUG
)

# Для использования логгера его нужно получить/создать функцией getLogger
LOG = logging.getLogger('app.basic')

# После этого можно использовать логгирование таким образом
LOG.debug('Отладочная информация')
LOG.info('Информационное сообщение')
LOG.warning('Предупреждение')
LOG.critical('Критическое сообщение')

LOG.info('Hello, world!')
LOG.warning('It seems to be a bug...')
LOG.critical('Critical bug in app! Hello, World!')