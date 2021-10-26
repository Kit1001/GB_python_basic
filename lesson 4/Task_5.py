"""
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.

Доработать скрипт: теперь он должен работать и из консоли
"""

import utils
import sys

if len(sys.argv) == 1:
    print('Польский злотый:', *utils.currency_rates('pln'))
    print('Белорусский рубль:', *utils.currency_rates('byn'))
else:
    print(utils.currency_rates(sys.argv[-1]))
