
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


class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, id_):
        super().__init__(last_name, first_name, middle_name, age)
        self.id_ = id_
        self.access = self._calculate_access()

    def _calculate_access(self):
        return sum(map(int, str(self.id_))) % 7


e1 = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 1234986)
print(e1.full_name(), e1.check_birthday(), e1.access)
