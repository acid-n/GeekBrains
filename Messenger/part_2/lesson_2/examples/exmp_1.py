# Простой класс с атрибутами и методом

class Worker:
    # класс работник
    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.rate = rate

    def total_profit(self):
        # расчет зарплаты
        return self.hours * self.rate


OBJ = Worker('Иван', 'Иванов', 10, 100)
print(OBJ.total_profit())

# Теперь попробуем отрицательное значение в атрибуте
OBJ = Worker('Петр', 'Петров', -10, 100)
print(OBJ.total_profit())