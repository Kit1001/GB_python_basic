"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани.
Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title, size):
        self.title = title
        self.size = size

    @abstractmethod
    def fabric_consumption(self, k1, k2):
        return self.size * k1 + k2


class Suit(Clothes):
    k1 = 2
    k2 = 0.3

    @property
    def fabric_consumption(self):
        return super().fabric_consumption(Suit.k1, Suit.k2)


class Coat(Clothes):
    k1 = 1 / 6.5
    k2 = 0.5

    @property
    def fabric_consumption(self):
        return super().fabric_consumption(Coat.k1, Coat.k2)


my_suit = Suit('Костюм', 6)
print(f'Расход ткани на костюм 6го размера: {my_suit.fabric_consumption: .2f}')

my_coat = Coat('Пальто', 185)
print(f'Расход ткани на пальто на рост 185: {my_coat.fabric_consumption: .2f}')
