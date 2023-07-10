'''
Задание №7
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку.
'''
import csv

import csv
import pickle

def csv_reader(file):
    with open(file, encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter=",")
        count = 0
        # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                print(f'{row[0]} {row[1]} {row[2]}')
            count += 1
        print(f'Всего в файле {count} строк.')
        str_pickle = pickle.dumps(file)
        print(str_pickle)


csv_reader('file.csv')

