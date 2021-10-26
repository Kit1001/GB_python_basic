"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
{
  100: (15, ['txt']),
  1000: (3, ['py', 'txt']),
  10000: (7, ['html', 'css']),
  100000: (2, ['png', 'jpg'])
}

Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

Комментарий: скрипт запускается из терминала, в качестве аргумента нужно передать путь до нужной папки
"""

import os
import sys
import json

# список размеров в байтах, для которых создаются позиции в словаре
size_list = (100, 1000, 10000, 100000)

# если путь до папки был указан с \ на конце - убираем его, т.к. он помешает корректно работать os.path.split()
directory = sys.argv[1] if sys.argv[1][-1] != "\\" else os.path.split(sys.argv[1])[0]

# создаем структуру словаря
summary = {}
for size in size_list:
    summary.setdefault(size, [0, []])

for root, dirs, files in os.walk(directory):
    for file in files:

        # проверяем есть ли у файла расширение
        if '.' in file:
            ext = file.rsplit('.', maxsplit=1)[-1]
        else:
            ext = None

        # увеличиваем счетчик кол-ва файлов и добавляем расширение файла в список в словаре summary, если оно есть
        f_size = os.stat(os.path.join(root, file)).st_size
        for size in size_list:
            if f_size < size:
                summary[size][0] += 1
                if ext and ext not in summary[size][1]:
                    summary[size][1].append(ext)
                break

# меняем тип значения в словаре со списка на кортеж по условию задачи
for key, val in summary.items():
    summary.update({key: tuple(val)})

with open(f'{os.path.split(directory)[-1]}_summary.json', 'w', encoding='utf-8') as f: json.dump(summary, f)

print('{')
for key, val in summary.items():
    print(f'{key}: {val}')
print('}')
