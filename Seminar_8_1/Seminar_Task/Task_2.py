'''
Задание №2
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
'''

import json
from pathlib import Path


def add_to_json():
    if Path('task_2.json').exists():
        with open('task_2.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
    else:
        file = {str(k): {} for k in range(1, 8)}
    while True:
        inp = input("Введите  через пробел: Имя, идентификатор, уровень доступа: ")
        if not inp:
            break
        name, id_, access = inp.split()
        file[access].update({id_: name})
        # file.setdefault(access, {}).update({id_: name})
    with open('task_2.json', 'w', encoding='utf-8') as f:
        json.dump(file, f)


add_to_json()
