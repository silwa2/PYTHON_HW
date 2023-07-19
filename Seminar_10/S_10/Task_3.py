# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п.
# на ваш выбор.
# Cвойство возраст должно быть недоступно для прямого обращения,
# но возможность получить текущий возраст должна присутствовать.

class Person:

    def __init__(self, last_name, first_name, middle_name, age):
        self.last_name, self.first_name, self.middle_name, self.__age = \
            last_name, first_name, middle_name, age

    def check_birthday(self):
        return self.__age

    def change_birthday(self):
        self.__age += 1

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'


r = Person('Root', 'Ivan', '222', 6)

print(r.change_birthday())
print(r.check_birthday())
print(r.full_name())
