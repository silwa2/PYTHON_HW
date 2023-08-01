class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = b
        self.shape = 'rectangle'
        if not b:
            self.b = a
            self.shape = 'square'

    def per(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def __add__(self, other):
        p1 = self.per()
        p2 = other.per()
        a1 = self.square()
        a2 = other.square()
        per = p1 + p2
        area = a1 + a2
        res_a1 = (per - (per ** 2 - 16 * area) ** 0.5) / 4
        res_a2 = (per + (per ** 2 - 16 * area) ** 0.5) / 4
        res_b = area / res_a1
        return Rectangle(res_a1, res_b)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b