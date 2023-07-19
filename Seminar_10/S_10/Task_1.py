'''
Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
'''
import math

class Circle:

    def __init__(self, radius: int = 1):
        self.radius = radius

    def len_circle(self):
        return 2 * math.pi * self.radius

    def share(self):
        return math.pi * self.radius ** 2


circle = Circle(3)
print(f'Длина окружности = {round(circle.len_circle(), 2)}\nПлощадь круга = {round(circle.share(), 2)}')
