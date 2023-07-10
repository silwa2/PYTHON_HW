"""
Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры
используйте генераторное выражение.

"""
from random import randint

__all__ = ['func']

def func(lover_limit, upper_limit, count):
    num = randint(lover_limit, upper_limit)
    count -= 1
    while count != -1:
        number = int(input(f"Введите число от {lover_limit} до {upper_limit}: "))
        if number == num:
            print("Вы угадали число - это ", number)
            break
        if number < num:
            print("Загаданное число больше ", number)
        else:
            print("Загаданное число меньше ", number)
        print(' ')
        print(f"Осталось {count} попыток")
        count -= 1


if __name__ == '__main__':  # используется как отладчик для того чтобы не запускалось в других файлах
    func(0, 150, 15)
