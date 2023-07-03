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

