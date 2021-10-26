"""
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...
@type_logger
def calc_cube(x):
   return x ** 3
# >>> a = calc_cube(5)
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
calc_cube(5: <class 'int'>)

Комментарий: Функция calc_sum считает сумму переданных аргументов, игнорируя ошибки
"""


from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = []
        for arg in args:
            result.append(f'{arg}: {type(arg)}')
        for key, val in kwargs.items():
            result.append(f'{key}: {val} {type(val)}')
        func_result = func(*args, **kwargs)
        print(f'{func.__name__}({", ".join(result)})')
        return f'{func_result} {type(func_result)}'

    return wrapper


@type_logger
def calc_sum(*args, **kwargs):
    summ = 0
    for arg in args:
        try:
            summ += arg
        except (ValueError, TypeError):
            pass
    return summ


print(calc_sum('Abc', 123, 123.123, keyarg=True))   # выводим результат работы функции с логгером
print(calc_sum.__name__)                            # проверяем .__name__  чтобы убедиться, что декоратор скрыт
