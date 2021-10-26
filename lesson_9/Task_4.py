"""
Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда);

опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    def __init__(self, speed, color, name, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police: bool = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 60:
            print(f'Скорость {self.speed}')
        else:
            print(f'Превышение скорости! {self.speed}, макс. 60')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police: bool = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 60:
            print(f'Скорость {self.speed}')
        else:
            print(f'Превышение скорости! {self.speed}, макс. 40')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police: bool = False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police: bool = True):
        super().__init__(speed, color, name, is_police)


toyota = PoliceCar(100, 'White', 'Toyota')
toyota.go()
toyota.stop()
toyota.show_speed()
print(toyota.__dict__)

honda = TownCar(80, 'Black', 'Honda')
honda.show_speed()
print(honda.__dict__)

lada = WorkCar(60, 'Red', 'Lada')
lada.show_speed()
print(lada.__dict__)
