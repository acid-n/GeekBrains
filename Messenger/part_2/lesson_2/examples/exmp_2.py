# Пробуем решить проблему традиционным способом - через геттеры и сеттеры

class Worker:
    # Делаем атрибуты защищенными
    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self._hours = hours
        self._rate = rate

    # Для создания свойства-геттера над свойством ставится аннотация @property
    @property
    def hours(self):
        # Геттер
        return self._hours

    # Сеттер
    # Для создания свойства-сеттера над свойством устанавливается аннотация имя_свойства_геттера.setter
    @hours.setter
    def hours(self, value):
        # Сеттер
        if value < 0:
            raise ValueError('Значение чаасов не может быть отрицательным')
        self._hours = value

    @property
    def rate(self):
        # Геттер
        return self._rate

    @rate.setter
    def rate(self, value):
        # Сеттер
        if value < 0:
            raise ValueError('Значение ставки не может быть отрицательным')
        self._rate = value

    def total_profit(self):
        # Вычисляем зарплату
        return self.hours * self.rate


OBJ = Worker('Иван', 'Иванов', 10, 100)
print(OBJ.total_profit())

OBJ = Worker('Иван', 'Иванов', -10, 100)
print(OBJ.total_profit())

OBJ.hours = 10
OBJ.rate = 100
print(OBJ.total_profit())

OBJ.hours = -10
OBJ.rate = 100
print(OBJ.total_profit())