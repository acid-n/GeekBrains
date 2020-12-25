# Простой метакласс
# Этот метакласс обеспечивает доступ своих классво к методу логгирования on_log

import sys
import logging

LOG = logging.getLogger('basic')
CRIT_HAND = logging.StreamHandler(sys.stderr)
FORMATTER = logging.Formatter("%(levelname)-7s %(asctime)s %(message)s")
CRIT_HAND.setFormatter(FORMATTER)
LOG.addHandler(CRIT_HAND)
LOG.setLevel(logging.DEBUG)


class Logging(type):
    # Метод on_log
    def on_log(cls):
        LOG.info(f'Данный метакласс фиксирует работу с классом {cls}')

    # Вызываем метакласс
    def __call__(self, *args, **kwargs):
        # Создаем новый класс как обычно
        cls = type.__call__(self, *args)

        # Определяем новый метод on_log для каждого из этих классов
        setattr(cls, "on_log", self.on_log)

        # возвращаем класс
        return cls


# Проверяем метакласс
class MyClass(metaclass=Logging):
    def fixing(self):
        self.on_log()


# Создаем экземпляр метакласса. Он должен автоматически содержать метод on_log хотя он не объявлен в классе вручную
# иными словами, он объявлен за нас метаклассом

MC = MyClass()
MC.fixing()