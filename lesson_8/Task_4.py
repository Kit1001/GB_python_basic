"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


# >>> a = calc_cube(5)
125
# >>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5


Примечание: сможете ли вы замаскировать работу декоратора?
"""
from functools import wraps


def val_checker(more_than_zero):
    def _val_checker(func):
        @wraps(func)
        def wrapper(arg):
            if not more_than_zero(arg):
                msg = f'wrong value {arg}'
                raise ValueError(msg)
            return func(arg)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube.__name__)   # проверяем что декоратор скрыт
print(calc_cube(5))         # результат нормальной работы функции
print(calc_cube(-5))        # передаем неправильное значение, получаем ValueError
