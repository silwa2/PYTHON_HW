'''
Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
'''

from random import randint, uniform

UPPER_LIMIT = 1000
LOVER_LIMIT = -1000


def file(filename, count):
    with open('Task_1.md', 'w', encoding='utf-8') as Task_1:
        for i in range(count):
            int_num = randint(LOVER_LIMIT, UPPER_LIMIT)
            float_num = uniform(LOVER_LIMIT, UPPER_LIMIT)
            Task_1.write(f'{int_num:>5} | {float_num:.3f}\n')


if __name__ == '__main__':
    file('Task_1.md', 30)
