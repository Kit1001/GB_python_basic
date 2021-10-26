"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый — с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


import re


class Date:
    r = re.compile(r'^([\d]+)-([\d]+)-([\d]{4})$')

    def __init__(self, date_string):
        r = Date.r
        if r.match(date_string):
            self.date = date_string
            print(r.match(date_string))
        else:
            print('Неверный формат')

    @classmethod
    def extract(cls, date_string):
        r = cls.r
        if r.match(date_string):
            day = int(r.match(date_string).groups()[0])
            month = int(r.match(date_string).groups()[1])
            year = int(r.match(date_string).groups()[2])
            return day, month, year
        else:
            print('Неверный формат')

    @staticmethod
    def validate(date_string):
        r = Date.r
        if r.match(date_string):
            day = int(r.match(date_string).groups()[0])
            month = int(r.match(date_string).groups()[1])
            year = int(r.match(date_string).groups()[2])

            leap_year = False
            if year % 4 == 0:
                leap_year = True

            months_with_30_days = [4, 6, 9, 11]
            if month in months_with_30_days:
                max_days = 30
            elif month == 2 and leap_year:
                max_days = 29
            elif month == 2:
                max_days = 28
            elif 0 < month < 13:
                max_days = 31
            else:
                return False

            if 0 < day <= max_days:
                return True
            else:
                return False
        else:
            print('Неверный формат')


print('Результат работы Date.extract() - кортеж из трех чисел, выведем объект и тип каждого элемента кортежа:')
for number in Date.extract('01-02-1954'):
    print(number, type(number))

print('')
print('Демонстрация работы метода Date.validate:')
print(f'Верна ли дата 29-02-1984: ', Date.validate('28-02-1984'))
print(f'Верна ли дата 29-02-1983: ', Date.validate('29-02-1983'))
print(f'Верна ли дата 00-03-1984: ', Date.validate('00-03-1984'))
print(f'Верна ли дата 05-54-1984: ', Date.validate('05-54-1984'))
print(f'Верна ли дата 05-01-54239: ', end="")
Date.validate('05-01-54239')
