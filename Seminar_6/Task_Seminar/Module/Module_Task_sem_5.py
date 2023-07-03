import random

__all__ = ['puzzle', 'puzzle_solut']
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


'''
Задача 5
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

'''


def puzzle_solut():
    dict_puzzle = {'Зимой и летом одним цветом': ['ель', 'елка', 'доллар'], 'Висит груша - нельзя скушать': ['груша', 'игрушка', 'лампочка']}

    for key, values in dict_puzzle.items():
        puzzle(key, values, random.randint(1, 5))
