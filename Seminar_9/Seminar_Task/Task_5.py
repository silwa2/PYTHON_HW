# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# декораторами для сохранения параметров,
# декоратором контроля значений и
# декоратором для многократного запуска.
# Выберите верный порядок декораторов.
from Task_3 import save_params
from Task_2 import rand_params
from Task_4 import count


@count(3)
@rand_params
@save_params
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

print(quiz(200, 100))