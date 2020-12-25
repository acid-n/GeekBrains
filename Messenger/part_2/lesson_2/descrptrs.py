import logging

logger = logging.getLogger('server')


# Дескриптор для описания порта
class Port:
    def __set__(self, instance, value):
        if not 1023 < value < 65536:
            logger.critical(f'Попытка запуска сервера с указанием неподходящего порта')
            exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
