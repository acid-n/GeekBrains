# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title=''):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Нам нужна {self.title} для записей в ежедневник.")


class Pencil(Stationery):
    def draw(self):
        print(f"Мы используем {self.title} для набросков в блокноте.")


class Handle(Stationery):
    def draw(self):
        print(f"А вот {self.title} мы используем для выделения фрагментов в книгах и журналах.")


pen = Pen("ручка")
pencil = Pencil("карандаш")
handle = Handle("маркер")

pen.draw()
pencil.draw()
handle.draw()