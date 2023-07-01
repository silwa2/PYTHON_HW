# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

__all__ = ['conflict','queens','queenprint']
import random

def conflict(state, col):
    # Конфликтная функция, строка - строка, столбец - столбец
    row = len(state)
    for i in range(row):
        if abs(state[i] - col) in (0, row - i):  # важный оператор
            return True
    return False


def queens(num=8, state=()):
    # Функция-генератор
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def queenprint(solution):
    # Функция печати
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(f'{line(pos)}')


for solution in list(queens(8)):
    print(solution)
