# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.
import json
import os
from functools import wraps


def save_params(func):
    func_name = func.__name__
    if os.path.exists(f'./{func_name}.json'):
        with open(f'./{func_name}.json', 'r', encoding='utf-8') as j:
            result_list = json.load(j)
    else:
        result_list = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        func_res = func(*args, **kwargs)
        result = {'args': args,
                  'kwargs': kwargs,
                  'result': func_res}
        result_list.append(result)
        with open(f'./{func_name}.json', "w", encoding="utf-8") as j:
            json.dump(result_list, j, indent=2)
        return func_res

    return wrapper

@save_params
def sum_num(a, b):
    return a + b


if __name__ == "__main__":
    print(sum_num(3, 5))
    print(sum_num(1, 1))
    print(sum_num(4, 6))