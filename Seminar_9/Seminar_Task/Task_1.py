# Создайте функцию-замыкание, которая принимает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
from random import randint


def game(secret, attempts):
    def quiz():
        for i in range(attempts):
            n = int(input(f"Попытка номер {i + 1}, попытайтесь отгадать число: "))
            if n > secret:
                turn = "Меньше"
            elif n < secret:
                turn = "Больше"
            else:
                return "Победа!"
            print(turn)
        else:
            return "Попыток больше нет, вы проиграли."

    return quiz


if __name__ == "__main__":
    quiz_game = game(randint(0, 100), 10)
    print(quiz_game.__name__)
    print(quiz_game())