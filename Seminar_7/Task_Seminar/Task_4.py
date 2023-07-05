'''
Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.

'''
from string import ascii_letters  # все буквы латинские abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
from random import randint, choices, randbytes


def new_file(extension: str, amount_file: int = 3, min_len_name: int = 5, max_len_name: int = 10,
             min_size_file: int = 256, max_size_file: int = 4096):
    for _ in range(amount_file):
        len_name = randint(min_len_name, max_len_name)
        file_name = ''.join(choices(ascii_letters, k=len_name)) + extension  # возвращает строку имя файла с расширением
        size = randint(min_size_file, max_size_file)
        with open(file_name, 'wb') as T4:
            T4.write(randbytes(size))


if __name__ == '__main__':
    new_file('.md', 4)
