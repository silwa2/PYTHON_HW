'''
Задание №1
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
Добавьте  строки документации для классов.
'''
import datetime


class MyStr(str):
    """
    My class  comment
    """
    d = 5

    def __new__(cls, value, author_name):
        """
        Создает экземпляр
        :param value:
        :param author_name:
        creation_time = datetime.datetime.now()
        """
        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.creation_time = datetime.datetime.now()
        return instance

    def __str__(self):
        return f'Имя: {self.author_name} , время: {self.creation_time}'

    def __repr__(self):
        return f'Mystr({self.author_name} , время: {self.creation_time})'

if __name__ == '__main__':
    s = MyStr("Строка", 'Илюша')
    print(s)
    print(repr(s))


    # print(s, s.author_name, s.creation_time)
    # print(s.upper())

    # print(MyStr.__doc__)
    # print(MyStr.__new__.__doc__)
    # print(help(MyStr))