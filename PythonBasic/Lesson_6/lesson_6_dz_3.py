# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


# реализовать базовый класс Worker (работник)
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Имя: {self.name}, Фамилия: {self.surname}")

    def get_total_income(self):
        result = self._income['wage'] + self._income['bonus']
        print(f"Доход: {result}")


# вызываем класс с параметрами класса Worker
a = Position("Kirill", "Bonusov", "manager", 100, 50)

# выводим полное имя работника
a.get_full_name()

# выводим доход работника с учетом премии
a.get_total_income()
