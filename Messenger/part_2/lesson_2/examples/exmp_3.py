# Дескриптор это атрибут объекта со связанным поведением, то есть такой атрибут,
# при доступе к которому его поведение переопределяется методом протокола дескриптора.
# Эти методы __get__, __set__ и __delete__.
#
# Проверим дескриптор

class NonNegative:
    # Этот класс поможет нам сделать атрибуты дескрипторами

    def __init__(self, my_attr):
        # Вместо my_attr на самом деле будет hours или rate
        self.my_attr = my_attr

    def __get__(self, instance, owner):
        # instance - экземпляр класса Worker
        # owner - клас Worker
        # instance.__dict__ - словарь атрибутов экземпляра класса
        # получаем значение из словаря атрибутов экземпляра класса
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        # instance - экземаляр класса Worker
        # value - присваиваемое значение, например 10 или 100 в нашем случае
        if value < 0:
            raise ValueError('Не может быть отрицательным')

        # присваиваем значение атрибуту, если оно прошло валидацию
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        # перехватываем удаление атрибута
        del instance.__dict__[self.my_attr]


class Worker:
    # Делаем атрибуты дескрипторами
    # сразу виден недостаток - приходится передавать конструктору класса имя атрибута
    hours = NonNegative('hours')
    rate = NonNegative('rate')

    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.rate = rate

    def total_profit(self):
        return self.hours * self.rate


OBJ = Worker('Иван', 'Иванов', 10, 100)
print(OBJ.total_profit())


OBJ = Worker('Иван', 'Иванов', -10, 100)
print(OBJ.total_profit())