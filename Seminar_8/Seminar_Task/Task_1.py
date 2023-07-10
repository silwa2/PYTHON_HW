# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json

def convert_to_json(path, new_path):
    res = {}
    with (
        open(path, "r", encoding="utf-8") as f,
        open(new_path, 'w', encoding='utf-8') as j
    ):
        for line in f:
            name, data = line.split(';')
            res[name.upper()] = data[:-1]

        return json.dump(res, j)


convert_to_json('C:\\Users\\79282\\PycharmProjects\\PYTHON_HW\\Seminar_7\\Task_Seminar\\Task_3.md',\
                'C:\\Users\\79282\\PycharmProjects\\PYTHON_HW\\Seminar_8\\Seminar_Task\\task_1.json')

