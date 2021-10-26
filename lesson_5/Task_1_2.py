"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""


def odd_nums_yield(num_max):
    """Решение задачи с помощью yield"""
    for num in range(1, num_max + 1, 2):
        yield num


def odd_nums_no_yield(num_max):
    """Решение задачи без помощи yield"""
    return (num for num in range(1, num_max + 1, 2))


odd_15 = odd_nums_yield(15)
print(type(odd_15), *odd_15)

odd_20 = odd_nums_no_yield(20)
print(type(odd_20), *odd_20)
