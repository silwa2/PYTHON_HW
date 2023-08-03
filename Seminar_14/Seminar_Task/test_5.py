# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину,
# а также вычисляющую периметр, площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
import unittest

from Task_5 import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(3, 5)

    def test_per(self):
        self.assertEqual(Rectangle(3, 5).per(), self.rectangle.per())

    def test_square(self):
        self.assertEqual(Rectangle(3, 5).square(), self.rectangle.square())

    def test_equal(self):
        self.assertEqual(Rectangle(3, 5), self.rectangle)