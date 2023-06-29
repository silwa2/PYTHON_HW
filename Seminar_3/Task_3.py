# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
#
# *Верните все возможные варианты комплектации рюкзака

import random

hike = {'палатка': 5,
        'котелок': 2,
        'веревка': 4,
        'еда': 3,
        'одежда': 2,
        'спальник': 3,
        }

print(f'Наш список вещей: {hike}')
BACKPACK = 10
summ = BACKPACK
new_backpack = {}

for key, value in hike.items():
    if value <= summ:
        summ -= value
        new_backpack[key] = value

print(f"Вместится в рюкзак не больше {BACKPACK} кг - это: {new_backpack}")

# Второй метод, случайные
# вещи
maximum_load = 8
counter = 0
List_artibute = []
while counter < maximum_load:
    key, value = random.choice(list(hike.items()))
    if key in List_artibute:
        continue
    if counter + value > maximum_load:
        break
    counter += value
    List_artibute += (str(key), str(value))

print(f'Вместится в рюкзак {List_artibute}, =  {counter} кг')