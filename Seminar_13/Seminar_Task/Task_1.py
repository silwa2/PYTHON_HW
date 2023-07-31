'''
Задание №1
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
'''


# 1 вариант решения
def get_number(massage: str) -> int | float:
    while True:
        try:
            num = float(input(massage))
        except ValueError as e:
            print(f"Неверный формат ввода, ошибка '{e}'\n")
        else:
            return int(num) if num.is_integer() else num

number = get_number('Введите число int или integer: ')
print(f'Ваше число {number}, тип числа {type(number).__name__}')


