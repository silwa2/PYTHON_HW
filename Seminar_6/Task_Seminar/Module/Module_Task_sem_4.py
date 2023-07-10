"""
Задача 4
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок
и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль,
если попытки исчерпаны.
"""

__all__ = ['puzzle']

def puzzle(puzle_text: str, solutions: list[str], tries: int) -> int:
    print(puzle_text)
    solutions =list(map(lambda x: x.lower(), solutions))
    num = 0
    while num < tries:
        user_input = input("Введен вариант ответа: ").lower()
        if user_input in solutions:
            num += 1
            return f'Правильно!!!'
        else:
            print(f'Не угадал! осталось {tries-num-1} попытки')
        num += 1
    return 0



# def puzzle(puzle_text: str) -> int | str:
#     print(f'Загадка: {puzle_text}')
#     attempt = 0
#     right_answer=1
#     num = 3
#     print(f"""
# Варианты ответа:
# 1. Груша.
# 2. Чашка.
# 3. Ложка.""")
#     while attempt < num:
#         user_input = int(input("введит вариант ответа: "))
#         if user_input == right_answer:
#             num -= 1
#             return 'Вы угадали!'
#         else:
#             print(f'Не угадал! Осталось {num-1} попытки')
#         num -= 1
#     return 'Вы не угадали! А жаль!'
#
#
# if __name__ == '__main__':
#
#     print(puzzle("Висит груша нельзя скушать"))

