# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать декорированную функцию со случайными числами из диапазонов.
from random import randint


def rand_params(func):
    start_rand = 1
    end_secret_rand = 100
    end_attempts_rand = 10
    min_diap = 0
    max_secret = 101
    max_attempts = 11

    def wrapper(secret, attempts):
        if not min_diap < secret < max_secret:
            secret = randint(start_rand, end_secret_rand)
        if not min_diap < attempts < max_attempts:
            attempts = randint(start_rand, end_attempts_rand)
        result = func(secret, attempts)
        return result

    return wrapper


@rand_params
def quiz(secret, attempts):
    print(f'Попытайтесь отгадать число за {attempts} попыток')
    for i in range(attempts):
        n = int(input(f"Попытка номер {i + 1}: "))
        if n > secret:
            turn = "Меньше"
        elif n < secret:
            turn = "Больше"
        else:
            return "Победа!"
        print(turn)
    else:
        return "Попыток больше нет, вы проиграли."


if __name__ == "__main__":
    print(quiz(101, 101))