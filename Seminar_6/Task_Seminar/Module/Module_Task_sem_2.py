"""
Задача 2 Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

"""


__all__ = ['func']

from random import randint


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
