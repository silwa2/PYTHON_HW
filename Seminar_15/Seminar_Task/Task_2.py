'''
Задание №2
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.
'''

import logging
import math

logging.basicConfig(filename='Task2.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)

def loggernator(func):
    def wrapper(a, b, c):
        res = func(a, b, c)
        logging.info(f'function {func.__name__} was called arguments {a, b, c} with {res}')
        return res
    return wrapper


@loggernator
def solve_square_equation(a, b, c):
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        x1 = (-b + math.sqrt(disc)) / (2 * a)
        x2 = (-b - math.sqrt(disc)) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif disc == 0:
        x = -b / (2 * a)
        return round(x, 2)


if __name__ == '__main__':
    solve_square_equation(4, 5, 6)
