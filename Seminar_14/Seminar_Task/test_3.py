# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import unittest

from Seminar_14.Seminar_Task.Task_1_2 import str_replace


class TestStringReplace(unittest.TestCase):

    def test_1(self):
        self.assertEqual(str_replace('asdgaa baga  aga'), 'asdgaa baga  aga')

    def test_2(self):
        self.assertEqual(str_replace('ASDgaa baga  aga'), 'asdgaa baga  aga')

    def test_3(self):
        self.assertEqual(str_replace('asdgaa baga - aga'), 'asdgaa baga  aga')

    def test_4(self):
        self.assertEqual(str_replace('asdgaa baga фыв aga'), 'asdgaa baga  aga')

    def test_5(self):
        self.assertEqual(str_replace('asdGaa baga 123фв agaфаф'), 'asdgaa baga  aga')


if __name__ == '__main__':
    unittest.main(verbosity=2)
