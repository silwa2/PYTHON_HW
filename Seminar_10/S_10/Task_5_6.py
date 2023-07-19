# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
class Animal:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_age(self, age):
        return self.age

    def get_name(self, name):
        return self.name


class Fish(Animal):
    def __init__(self, name, age, depth):
        super().__init__(name, age)
        self.depth = depth
        self.type = self.check_type()

    def check_type(self):
        return ("Мелководная", "Глубоководная")[self.depth > 1000]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nГлубина: {self.depth}\nТип: {self.type}\n'


class Bird(Animal):
    def __init__(self, name, age, wings):
        super().__init__(name, age)
        self.wings = wings
        self.type = self.check_type()

    def check_type(self):
        return ("Небольшой размах", "Большой размах")[self.wings > 3]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nРазмах крыльев: {self.wings}\nТип: {self.type}\n'


class Mammals(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight
        self.type = self.check_type()

    def check_type(self):
        return ("Мелкий", "Крупный")[self.weight > 100]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nВес: {self.weight}\nТип: {self.type}\n'


f = Fish('Nemo', 2, 100)
b = Bird('Kesha', 5, 4)
m = Mammals('Pumba', 10, 105)

print(f)
print(b)
print(m)

