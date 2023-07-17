# Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали.
# Превратите функции в методы класса. Задачи должны решаться через вызов методов экземпляра.


# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

class File_path:
    def __init__(self):
        self.text = text

    def file_path(self):
        *path, name = text.split('\\')
        name = list(name.split('.'))
        path = '\\'.join(path)
        expansion = name[1]
        return f'ПУТЬ: {path}, ИМЯ ФАЙЛА: {name[0]}, РАСШИРЕНИЕ: {expansion}'


text = r'C:\Users\79282\PycharmProjects\PYTHON_HW\Seminar_1\Task_1.py'
print(File_path.file_path(text))
