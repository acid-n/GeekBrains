# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    # определяем метод running с бесконечным циклом и выводом цвета сфетофора
    # указываем задержку в секундах для каждого цвет (красный - 7, желтый - 2 и зеленый - 7 секунд)
    # указываем для каждого цвета светофора, цвет текста
    def running(self):
        while True:
            print(f"\033[31m {self.__color[0]}")
            sleep(7)
            print(f"\033[33m {self.__color[1]}")
            sleep(2)
            print(f"\033[32m {self.__color[2]}")
            sleep(7)
            print(f"\033[33m {self.__color[1]}")
            sleep(2)


color = ["Красный", "Желтый", "Зеленый"]

a = TrafficLight(color)

a.running()