# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9], ]

print('Исходная матрица')
for element in matrix:
    print(*element, sep='\t')

print()

print('Транспонированная матрица')
for element in zip(*matrix):
    print(*element, sep='\t')
