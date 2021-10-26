"""
Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не программно);
предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

Комментарий:
В конфиге папки отмечены двоеточием на конце, уровень вложенности определяется отступами с помощью пробелов
или табуляции - 4 пробела или одна табуляция на каждый уровень вложенности.
Если корневая папка уже существует - все совпадающие в ней файлы будут перезаписаны. Перед этим у пользователя
запрашивается подтверждение.
"""

import os


def count_indents(string):
    """" Функция для подсчета количества отступов в строчке конфига, используется для определения уровня вложенности"""
    counter = 0
    whitespace_counter = 0
    while counter < len(string):
        if string[counter] == chr(32):
            whitespace_counter += 1
        elif string[counter] == chr(9):
            whitespace_counter += 4
        else:
            break
        counter += 1
    return whitespace_counter


script_path = ''            # в этой переменной хранится актуальный путь до объекта
last_dir = None
indent = 0

try:
    with open('config.yaml', 'r', encoding='utf-8') as f:
        lines = f.readlines()
except FileNotFoundError:
    print("Не найден файл config.yaml")
    exit()

for line in lines:
    object_name = line.strip().strip(':')

    if line == ' ---\n':        # игнорируем начало файла
        continue

    # Если корневая папка уже существует, запрашиваем подтверждение у пользователя
    if indent == 0 and os.path.exists(object_name):
        confirm = input(f'Папка {object_name} уже существует, все содержимое будет перезаписано.'
                        f' Чтобы продолжить введите "yes"\n')
        if confirm != 'yes':
            exit(1)

    # С помощью отступов определяем изменился ли уровень вложенности. Соответственно изменяем script_path
    # либо добавляя к нему последнюю созданную папку(last_dir), либо убирая папки из пути.
    if indent < count_indents(line):
        script_path = os.path.join(script_path, last_dir)
        indent = count_indents(line)
    elif indent > count_indents(line):
        while indent != count_indents(line):
            script_path = os.path.split(script_path)[0]
            indent -= 4

    # Папки в конфиге обозначены двоеточием на конце, создаем либо папку, либо файл по пути в script_path
    # Если создать объект не получилось (например, недостаточно прав), выходим из скрипта
    if line.strip()[-1] == ':':
        try:
            os.makedirs(os.path.join(script_path, object_name), exist_ok=True)
        except OSError as e:
            print(f'Ошибка при создании папки {os.path.join(script_path, object_name)}: {e}')
            exit()
        last_dir = object_name
    else:
        try:
            with open(os.path.join(script_path, object_name), 'w', encoding='utf-8') as f:
                f.write('')
        except OSError as e:
            print(f'Ошибка при записи файла {os.path.join(script_path, object_name)}: {e}')
            exit()
print('Стартер был успешно создан!')
