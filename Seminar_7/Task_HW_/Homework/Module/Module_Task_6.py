'''
Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
'''

from Seminar_7.Task_HW.Homework.Module.Module_Task_5 import expansion_files
from pathlib import Path
import os


def create_dir(name_dir: str):
    name = Path(Path.cwd() / name_dir)
    if not name.exists():  # проверка на наличие директория
        name.mkdir()  # создает директорий с именем name_dir в текущем директории

    os.chdir(name)  # переходим в созданный каталог сделав его текущим


if __name__ == '__main__':
    create_dir('Zorro')
    my_dict = {'.rar': 1, '.torrent': 1, '.avi': 1, '.pdf': 1}
    expansion_files(my_dict)

