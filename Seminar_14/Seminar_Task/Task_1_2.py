# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.
#
# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import string

LETTERS = string.ascii_letters + " "


def str_replace(text):
    """
    Модифицируем строку
    :param text:
    :return:
    >>> str_replace('asdgaa baga  aga')
    'asdgaa baga  aga'
    >>> str_replace('ASDgaa baga  aga')
    'asdgaa baga  aga'
    >>> str_replace('asdgaa baga - aga')
    'asdgaa baga  aga'
    >>> str_replace('asdgaa baga фыв aga')
    'asdgaa baga  aga'
    >>> str_replace('asdGaa baga 123фв agaфаф')
    'asdgaa baga  aga'
    """
    return "".join(i for i in text if i in LETTERS).lower()


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
