'''
Задание №2
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений
'''

def get_dict(my_dict, key, value='Такого ключа нет'):
    try:
        return my_dict[key]
    except KeyError as e:
        return value


if __name__ == '__main__':
    my_dict = {1: 'one', 2: 'two'}
    req_values = get_dict(my_dict, 3)
    print(req_values)
