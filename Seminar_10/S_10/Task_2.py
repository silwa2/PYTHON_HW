'''
Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
'''

class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = b
        self.shape = 'rectangle'
        if not b:
            self.b = a
            self.shape = 'square'

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b


renctagle = Rectangle(10, 2)
print(renctagle.perimetr(), renctagle.square())



















