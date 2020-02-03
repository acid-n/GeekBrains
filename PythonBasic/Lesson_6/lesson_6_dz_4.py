# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


# реализовать базовый класс Car
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        self.direction = direction
        print(f"Машина повернула {self.direction}")

    def show_speed(self):
        print(f"Скорость автомобиля: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость автомобиля {self.speed}. Автомобиль привысил скорость.")
        else:
            print(f"Скорость автомобиля: {self.speed}")


class SportCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость автомобиля {self.speed}. Это спортивный автомобиль. Может себе позволить.")
        else:
            print(f"Скорость автомобиля: {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость автомобиля {self.speed}. Это городской автомобиль и он привысил скорость.")
        else:
            print(f"Скорость автомобиля: {self.speed}")


class PoliceCar(Car):
    # берем все что передали и создаем с этими параметрами Car, плюс добавляем сюда is_police
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, is_police=True)

    def show_speed(self):
        if self.speed > 60 and self.is_police == True:
            print(f"Скорость автомобиля {self.speed}. Это полицейская машина. Идет погоня.")
        else:
            print(f"Скорость полицейского автомобиля: {self.speed}")


town_car = TownCar(80, 'Blue', 'Lada')
sport_car = SportCar(80, 'Red', 'Porsche')
work_car = WorkCar(60, 'Yellow', 'Volvo')
police_car = PoliceCar(120, 'Black', 'Maybach')

print(f"\nАвтомобиль {town_car.name}, цвета {town_car.color}.")
town_car.go()
town_car.show_speed()
town_car.turn("налево")
town_car.stop()

print(f"\nАвтомобиль {sport_car.name}, цвета {sport_car.color}.")
sport_car.go()
sport_car.show_speed()
sport_car.turn("направо")
sport_car.stop()

print(f"\nАвтомобиль {work_car.name}, цвета {work_car.color}.")
work_car.go()
work_car.show_speed()
work_car.turn("направо")
work_car.stop()

print(f"\nАвтомобиль {police_car.name}, цвета {police_car.color}.")
police_car.go()
police_car.show_speed()
police_car.turn("направо")
police_car.stop()
