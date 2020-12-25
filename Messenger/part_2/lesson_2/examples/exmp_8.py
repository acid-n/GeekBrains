# Пример метакласса, переопределяющего поведение методов __new__ и __init__ своих классов

class MyMetaClass(type):
    # Вызывается для создания экземпляра класса, перед вызовом __init__
    def __new__(cls, name, bases, dct):
        print(f'Выделение памяти для класса {name},\n'
              f'имеющего кортеж базовых классов {bases},\n'
              f'и словарь атрибутов {dct}')
        return type.__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f'Инициализация класса {name}')
        super(MyMetaClass, cls).__init__(name, bases, dct)


# Родитель 1
class Parent_1():
    pass


# Родитель 2
class Parent_2():
    pass


# Пользовательский класс
class MyClass(Parent_1, Parent_2, metaclass=MyMetaClass):
    my_attr = 10


MC = MyClass()
