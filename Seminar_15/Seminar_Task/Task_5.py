'''
Задание №5
Дорабатываем задачу 4.
Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5.
'''

from Task_4 import text_to_date
import argparse
from datetime import datetime

if __name__ == '__main__':
    months = {1: 'янв', 2: 'фев', 3: 'мар', 4: 'апр', 5: 'май', 6: 'июн', 7: 'июл', 8: 'авг', 9: 'сен', 10: 'окт',
              11: 'ноя', 12: 'дек'}
    weekdays = {1: 'вто', 2: 'сре', 3: 'чет', 4: 'пят', 5: 'суб', 6: 'вос', 7: 'пон'}

    parser = argparse.ArgumentParser(description="Получаем строку с датой")
    parser.add_argument('-day', type=str, default='1')
    parser.add_argument('-weekday', type=str, default=datetime.now().weekday())
    parser.add_argument('-month', type=str, default=datetime.now().month)

    args = parser.parse_args()
    # можно так но без чисел только названия масяцев и дней
    # rez = text_to_date(f'{args.day}, {args.weekday}, {args.month}')
    # print(f'Передано в скрипт: {args}')
    # print(f'{args.day} {args.weekday} {args.month}: ', rez)

    # или можно так
    weekday = weekdays[int(args.weekday)] if args.weekday.isdigit() and int(
        args.weekday) in weekdays else args.weekday  # неделю можно вводить числом
    month = months[int(args.month)] if args.month.isdigit() and int(
        args.month) in months else args.month  # месяц можно вводить числом

    print(f'{args.day} {weekday} {month}: ', text_to_date(f'{args.day} {weekday} {month}'))

# запуск с командной строки: python Task_5.py -day='3-й' -weekday='среда'
# запуск с командной строки: python Task_5.py -day='3-й' -weekday=3
# запуск с командной строки: python Task_5.py -day='3-й' -weekday=3 -month=3
