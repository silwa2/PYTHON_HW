'''
Задача 6
Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и
число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря
в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.

'''


__all__ = ['puzzle', 'puzzle_solut', 'puzzle_solver', 'puzzle_dict']


_solutions = {} # словарь protected (защищенный)
puzzle_dict = {'Зимой и летом одним цветом': ['ель', 'елка', 'доллар'], 'Висит груша - нельзя скушать': ['груша', 'игрушка', 'лампочка']}


import random

def puzzle(puzle_text: str, solutions: list[str], tries: int) -> int:
    print(puzle_text)
    solutions =list(map(lambda x: x.lower(), solutions))
    num = 0
    while num < tries:
        user_input = input("введит вариант ответа: ").lower()
        if user_input in solutions:
            num = num + 1
            return num
        else:
            print('не угадал!')
        num += 1
    return 0


def puzzle_solut():
    dict_puzzle = {'Зимой и летом одним цветом': ['ель', 'елка', 'доллар'], 'Висит груша - нельзя скушать': ['груша', 'игрушка', 'лампочка']}

    for key, values in dict_puzzle.items():
        puzzle(key, values, random.randint(1, 5))

def puzzle_solver(puzzle_text: str, tries: int):
    num = puzzle(puzzle_text,puzzle_dict[puzzle_text], tries)
    _solutions[puzzle_text] = [num, True if num else False]


def show_rezult():
    for k, v in _solutions.items():
        print(k, v)