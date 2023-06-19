# Напишите программу, которая принимает две строки вида
# “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.


import fractions

a1, b1 = map(int, input("Введите первую дробь вида a/b: ").split('/'))
a2, b2 = map(int, input("Введите вторую дробь вида a/b: ").split('/'))

# Вычисление суммы дроби
numerator = (b2 * a1) + (b1 * a2)
denominator = b1 * b2
if denominator == 0:
    result = 'Знаменатель не должен быть нулевым'
elif (a1 + a2) == 0:
    result = 'Сумма равна 0'

else:
    if fractions.Fraction(numerator, denominator) == fractions.Fraction(a1, b1) + fractions.Fraction(a2, b2):
        result = 'Сумма дроби равна: {}/{}'.format(numerator, denominator)
print(result)

# Вычисление произведения дроби
numerator = a1 * a1
denominator = b1 * b1
if denominator == 0:
    result = 'Знаменатель не должен быть нулевым'
elif numerator == 0:
    result = 'Произведение равно 0'
else:
    if fractions.Fraction(a1 * a2, b1 * b2) == fractions.Fraction(a1, b1) * fractions.Fraction(a2, b2):
        result = 'Произведение дроби равно: {}/{}'.format(a1 * a2, b1 * b2) \
            if numerator != denominator else 'Произведение равно {}'.format(int(numerator / denominator))
print(result)
