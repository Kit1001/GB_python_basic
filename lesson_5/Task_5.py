"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке,например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
"""

import collections
import time

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start = time.perf_counter()
unique = set()
tmp = set()
for num in src:
    if num in tmp:
        unique.discard(num)
    else:
        unique.add(num)
    tmp.add(num)
result = [num for num in src if num in unique]
print(result, '\n', time.perf_counter() - start)


start = time.perf_counter()
num_count = collections.Counter(src)
result = [num for num in src if num_count[num] == 1]
print(result, '\n', time.perf_counter() - start)
