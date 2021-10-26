"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
"""

import os
import shutil

directory = os.walk('my_project')
dest = os.path.join('my_project', 'templates')

for path, dirs, files in directory:
    for file in files:
        # проверяем, что у файла есть расширение
        if '.' in file:
            ext = file.rsplit('.', maxsplit=1)[-1]
        else:
            continue

        # копируем файл в папку my_project\templates создавая для него папку с именем, как у родительской
        # если точно такой же файл уже существует, выводим сообщение для пользователя
        file_dir = os.path.split(path)[-1]
        if ext == 'html':
            os.makedirs(os.path.join(dest, file_dir), exist_ok=True)
            try:
                shutil.copy(os.path.join(path, file), (os.path.join(dest, file_dir)))
            except shutil.SameFileError:
                print(f'Такой же файл {file} уже существует в папке {os.path.join(dest, file_dir)}')
